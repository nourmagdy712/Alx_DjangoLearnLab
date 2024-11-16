from django.apps import AppConfig
from django.db.models import Q


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        from django.contrib.auth.models import Group, Permission

        # Create groups if they don't exist
        editors, created = Group.objects.get_or_create(name='Editors')
        viewers, created = Group.objects.get_or_create(name='Viewers')
        admins, created = Group.objects.get_or_create(name='Admins')

        # Assign custom permissions to groups
        permissions = Permission.objects.filter(Q(codename__in=['can_view', 'can_create', 'can_edit', 'can_delete']))

        editors.permissions.set(permissions.filter(codename__in=['can_create', 'can_edit']))
        viewers.permissions.set(permissions.filter(codename__in=['can_view']))
        admins.permissions.set(permissions.filter(codename__in=['can_create', 'can_edit', 'can_delete']))

        pass
