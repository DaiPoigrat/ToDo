from django.db import models
from datetime import date
from django.utils.timezone import now


# Create your models here.

def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user{0}_{1}'.format(instance.id, filename)


class Users(models.Model):
    username = models.CharField("Username", max_length=20)
    mail = models.EmailField("Email")
    password = models.CharField("Password", max_length=20)
    profile_photo = models.ImageField(default="app/images/empty.webp", upload_to='app/images/')

    @property
    def user_id(self):
        return self.id

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.mail


class TodoList(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=50)
    text = models.TextField("Text")
    date = models.DateField(default=now())
    # point = models.BooleanField("Point", default=False)
    passed = models.BooleanField()

    def __str__(self):
        return self.user.mail + '  --//--  ' + self.name
