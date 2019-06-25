# Rest framework imports
from rest_framework import response, status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

# obnk
from models import User
from serializers import UserSerializer, AuthTokenEmailSerializer
from response_texts import get_response_text, PASSWORD_REQUIRED, WRONG_UUID, \
    USER_NOT_EXISTS

# Python
from exceptions import ValueError
import uuid


class SignUp(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, format=None):
        """
        Creates a new user with the given data in json format.
        Returns the newly generated token for the new user.

        Email, password and user_type must be sent.
        """
        data = request.data
        context = {'request': request}
        serializer = UserSerializer(data=data, context=context)
        if not data.get("password"):
            return response.Response(get_response_text(PASSWORD_REQUIRED),
                                     status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            # Hash password and create token for this user
            user = serializer.save()
            user.set_password(data['password'])
            user.save()
            token = Token.objects.create(user=user)
            result = {"token": token.key}
            return response.Response(result,
                                     status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = AuthTokenEmailSerializer

    def post(self, request):
        """Sends the authentication token if the provided credentials are
        correct. Email and password must be sent.

        """
        context = {'request': request}
        deserializer = self.serializer_class(data=request.data,
                                             context=context)
        if deserializer.is_valid():
            user_email = deserializer.validated_data['email'].lower()
            user = User.objects.get(email=user_email)
            token, _ = Token.objects.get_or_create(user=user)
            return response.Response({'token': token.key})
        return response.Response(deserializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)


class OwnUserProfile(APIView):

    def patch(self, request):
        """
        Edit requester user's profile
        """
        user = request.user
        data = request.data
        deserializer = UserSerializer(user,
                                      data=data,
                                      partial=True)
        if deserializer.is_valid():
            if ('password' in data):
                user = request.user
                user.set_password(data['password'])
                user.save()
            deserializer.save()
            serializer = UserSerializer(deserializer.instance)
            return response.Response(serializer.data, status.HTTP_200_OK)
        return response.Response(deserializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        Get requester user's profile info
        """
        user = request.user
        context = {"request": request}
        serializer = UserSerializer(user, context=context)
        return response.Response(serializer.data)


class UserProfile(APIView):

    def get(self, request, user_uuid):
        """
        Get the profile belonging to the provided user_uuid
        """
        try:
            save_uuid = uuid.UUID(user_uuid)
        except ValueError:
            return response.Response(get_response_text(WRONG_UUID),
                                     status=status.HTTP_400_BAD_REQUEST)
        user_exists = User.objects.filter(uuid=save_uuid)
        if user_exists:
            user = user_exists[0]
            serializer = UserSerializer(user)
            return response.Response(serializer.data)
        else:
            return response.Response(get_response_text(USER_NOT_EXISTS),
                                     status=status.HTTP_400_BAD_REQUEST)
