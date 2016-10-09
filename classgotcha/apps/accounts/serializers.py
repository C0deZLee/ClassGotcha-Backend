from model import Account
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = (
			'id', 'email', 'username', 'first_name', 'last_name', 'gender', 'birthday', 'school_year', 'major',
			'avatar')
