from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, username, full_name, password):
        if not full_name:
            raise ValueError('users must have Full Name')

        user = self.model(username=username, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, username, password):
        user = self.create_user(full_name, username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
