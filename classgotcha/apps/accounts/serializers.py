from models import Account
from rest_framework import serializers
from ..posts.models import Moment


class FullAccountSerializer(serializers.ModelSerializer):
	moments = serializers.PrimaryKeyRelatedField(many=True, queryset=Moment.objects.all())
	friends = serializers.PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())

	class Meta:
		model = Account
		fields = (
			'id', 'email', 'username', 'first_name', 'last_name', 'gender', 'birthday', 'school_year', 'major',
			'avatar', 'moments', 'friends')


class BasicAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = (
			'id', 'email', 'username', 'first_name', 'last_name', 'gender', 'birthday', 'school_year', 'major',
			'avatar')


class AccountMomentAccountSerializer(serializers.ModelSerializer):
	moments = serializers.PrimaryKeyRelatedField(many=True, queryset=Moment.objects.all())

	class Meta:
		model = Account
		fields = ['moments']
