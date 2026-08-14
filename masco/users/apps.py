# from django.apps import AppConfig


# class UsersConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'masco.users'

#     def ready(self):
#         import masco.users.signals



from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'masco.users'

    def ready(self):
        import masco.users.signals  # ✅ loads signal on startup