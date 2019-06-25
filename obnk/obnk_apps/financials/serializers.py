# Rest-framework imports
from rest_framework import serializers

# OBnk
from models import Transfer


class TransferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transfer
        exclude = ()
