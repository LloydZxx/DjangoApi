from rest_framework import serializers
from .models import User,Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','phone','profile_picture','address']

#User
class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id','email','position','is_activate','profile','password']

        #password response htl hmr ma pya buu
        extra_kwargs = {'password' : {'write_only' : True}}

     #user a thit phan tee tae a khar password ko hash lote py poh create method ko override lote ml
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
            user.save()
            return user
        

# Custom Claim Token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        #token htl hmr user email ko hte chn yn
        token['email'] = user.email
        #ta chr fields twy ko ll hte ng pr tl

        return token
    
