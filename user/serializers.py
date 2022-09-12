from django.contrib.auth.models import User
from .models import uSleep
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class newSleepSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user_details')
    sleepStart = serializers.CharField()
    sleepEnd = serializers.CharField()
    currentDate = serializers.CharField()
    duration = serializers.CharField()

    class Meta:
        model = uSleep
        fields = ['id', 'sleepStart', 'sleepEnd', 'duration', 'user','currentDate']
        extra_kwargs = {'user': {'read_only': True}, 'id': {'read_only': True}}
        depth = 2

    def create(self, validated_data):
        sleep = uSleep(
            sleepStart = validated_data['sleepStart'],
            sleepEnd = validated_data['sleepEnd'],
            duration =validated_data['duration'],
            currentDate =validated_data['currentDate'],
            user = self.context['request'].user
        )
        sleep.save()
        return sleep

    def get_user_details(self, item):
        # print(f"first_name:- {item.user.first_name}")
        user_details = f'{item.user.first_name} {item.user.last_name}'
        return user_details
