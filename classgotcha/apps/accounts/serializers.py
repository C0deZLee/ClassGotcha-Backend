from model import Account
from rest_framework import serializers
from ..moments.model import Moment


class AccountSerializer(serializers.ModelSerializer):
	moments = serializers.PrimaryKeyRelatedField(many=True, queryset=Moment.objects.all())

	class Meta:
		model = Account
		fields = (
			'id', 'email', 'username', 'first_name', 'last_name', 'gender', 'birthday', 'school_year', 'major',
			'avatar', 'moments')
