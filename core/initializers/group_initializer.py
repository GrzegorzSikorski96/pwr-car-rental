from django.contrib.auth.models import Group, Permission
from django.conf import settings
import json


class GroupInitializer:
    USER_GROUPS_FILENAME = 'user_groups.json'

    def initialize(self):
        pass
        user_groups_file = open(settings.CONFIG_FOLDER + self.USER_GROUPS_FILENAME, mode='r')
        groups = json.load(user_groups_file)
        for group, permissions in groups.items():
            group_object, created = Group.objects.get_or_create(name=group)
            group_object.permissions.clear()
            for permission in permissions:
                app_label, codename = permission.split('.')
                database_permission = Permission.objects.get(content_type__app_label=app_label, codename=codename)
                group_object.permissions.add(database_permission)
