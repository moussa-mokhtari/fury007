from models import Profile ,Phone,Address 
from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User 

class PhoneSerializer(serializers.ModelSerializer): 
      class Meta:
            model=Phone
            fields=('id','number_phone','country_code','created_at','updated_at')

class AddressSerializer(serializers.ModelSerializer): 
      class Meta:
            model=Address
            fields=('id','country','state','city','street','postal_code','created_at','updated_at')
class UserSerializer(serializers.ModelSerializer):
      class Meta:
            model=User            
class ProfileSerializer(serializers.ModelSerializer):
    user= UserSerializer(many=False)
    phones= PhoneSerializer(many=True)
    addresses=AddressSerializer(many=True)
    class Meta:
        model = Profile
        fields = ('id', 'user','phones','addresses')
