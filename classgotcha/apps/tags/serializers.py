from rest_framework import serializers
from models import Tag


class ClassFolderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('content', 'parent', 'children')


ClassFolderSerializer._declared_fields['children'] = ClassFolderSerializer()
