import django
__all__ = ['User']

# Django 1.5+ compatibility
if django.VERSION >= (1, 5):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    def get_user_set(group):
        related_query_name = User.groups.field.related_query_name
        return getattr(group, '%s_set' % related_query_name)
else:
    from django.contrib.auth.models import User
    get_user_model = lambda:User
    def get_user_set(group):
        return group.user_set
