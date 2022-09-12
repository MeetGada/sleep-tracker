from django.contrib.auth.models import User
from django.db.models import fields
from .models import uSleep
from rest_framework import serializers
from datetime import datetime

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

    class Meta:
        model = uSleep
        fields = ['id', 'sleepStart', 'sleepEnd', 'duration', 'user']
        extra_kwargs = {'user': {'read_only': True}, 'id': {'read_only': True}}
        depth = 2

    def create(self, validated_data):
        print(f"validated_data['sleepStart']:- {datetime.strptime(validated_data['sleepStart'], '%Y-%m-%dT%H:%M')}\n")
        # print(f"self.context['request']['data']:- {self.context['POST']}\n\n")
        sleep = uSleep(
            sleepStart = datetime.strptime(validated_data['sleepStart'], '%Y-%m-%dT%H:%M'),
            sleepEnd = datetime.strptime(validated_data['sleepEnd'], '%Y-%m-%dT%H:%M'),
            duration = datetime.strptime(validated_data['sleepEnd'], '%Y-%m-%dT%H:%M') - datetime.strptime(validated_data['sleepStart'], '%Y-%m-%dT%H:%M'),
            user = self.context['request'].user
        )
        sleep.save()
        return sleep

    def get_user_details(self, item):
        # print(f"first_name:- {item.user.first_name}")
        user_details = f'{item.user.first_name} {item.user.last_name}'
        return user_details


class sleepSerializer(serializers.ModelSerializer):
    sleepStart = serializers.DictField()
    sleepEnd = serializers.DictField()
    class Meta:
        model = uSleep
        fields = ['id', 'sleepStart', 'sleepEnd', 'duration','user']

    def create(self, validated_data):
        date_ = validated_data['sleepStart']['date']
        sleepStart = f"{date_['year']}-{date_['month']}-{date_['day']} {validated_data['sleepStart']['hrs']}:{validated_data['sleepStart']['mins']}:{validated_data['sleepStart']['sec']}"
        date_ = validated_data['sleepEnd']['date']
        sleepEnd = f"{date_['year']}-{date_['month']}-{date_['day']} {validated_data['sleepEnd']['hrs']}:{validated_data['sleepEnd']['mins']}:{validated_data['sleepEnd']['sec']}"
        # print(f"{sleepStart}, {sleepEnd}\n\nself.data:- {self.context['request'].user}\n\n\n")
        print(f"self.context['request']['data']:- {self.context['request'].POST}\n\n\n")
        sleep = uSleep(
            sleepStart = datetime.strptime(sleepStart, '%Y-%m-%d %H:%M:%S'),
            sleepEnd = datetime.strptime(sleepEnd, '%Y-%m-%d %H:%M:%S'),
            duration = datetime.strptime(sleepEnd, '%Y-%m-%d %H:%M:%S') - datetime.strptime(sleepStart, '%Y-%m-%d %H:%M:%S'),
            user = self.context['request'].user
        )
        # sleep.save(commit=False)
        return sleep


class sendSleepSerializer(serializers.ModelSerializer):
    sleepStart = serializers.CharField(required=False)
    sleepEnd = serializers.CharField(required=False)
    duration = serializers.CharField(required=False)

    class Meta:
        model = uSleep
        fields = ['id', 'sleepStart', 'sleepEnd', 'duration', 'user']
        extra_kwargs = {'user': {'read_only': True}, 'id': {'read_only': True}}