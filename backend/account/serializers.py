from django.utils import timezone
from rest_framework import serializers

from account.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        groups = validated_data.pop('groups')
        user_permissions = validated_data.pop('user_permissions')

        profile = Profile.objects.create(**validated_data)
        profile.set_password(validated_data.get('password'))
        profile.last_login = timezone.now()

        profile.groups.add(*groups)
        profile.user_permissions.add(*user_permissions)

        profile.save(update_fields=['last_login', 'password'])

        return profile
