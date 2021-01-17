from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    
    # for signal 
    # recomedation in documents
    def ready(self):
        import users.signals