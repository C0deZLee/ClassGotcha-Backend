from rest_framework import serializers
from models import Tag


class ClassFolderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('name',)


# ClassFolderSerializer._declared_fields['children'] = ClassFolderSerializer()

class BasicTagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('name',)
