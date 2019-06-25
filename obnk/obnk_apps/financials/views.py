# Rest framework imports
import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from models import Transfer, User
from obnk_apps.users.response_texts import get_response_text, WRONG_UUID, \
    USER_NOT_EXISTS
from rest_framework import response, status
from rest_framework.views import APIView


class Transfers(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        """
        Creates a new transfer between two users.
        Returns if the transaction was succesful.
        """

        source_user_id = request.data['source_user']
        target_user_id = request.data['target_user']
        amount = request.data['transfer_amount']

        try:
            source_uuid = uuid.UUID(source_user_id)
            target_uuid = uuid.UUID(target_user_id)
        except ValueError:
            return response.Response(get_response_text(WRONG_UUID),
                                     status=status.HTTP_400_BAD_REQUEST)

        # Prevent other transactions to modify source or target users
        # account balance to prevent concurrent modification issues.
        with transaction.atomic():
            try:
                source_user = User.objects.select_for_update().get(
                    pk=source_uuid)
                target_user = User.objects.select_for_update().get(
                    pk=target_uuid)
            except ObjectDoesNotExist:
                return response.Response(get_response_text(USER_NOT_EXISTS),
                                         status=status.HTTP_400_BAD_REQUEST)

            if source_user.account_balance >= amount:
                source_user.account_balance -= amount
                target_user.account_balance += amount

                source_user.save()
                target_user.save()

            else:
                result = {'message': 'not enough money to fund transfer'}
                return response.Response(result,
                                         status=status.HTTP_400_BAD_REQUEST)

            result = {'current_balance': source_user.account_balance}
            return response.Response(result, status=status.HTTP_201_CREATED)

    def get(self, request):

        transfers = Transfer.objects.all()
        result = {'data': transfers}
        return response.Response(result, status=status.HTTP_200_OK)
