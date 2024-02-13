from django.db import models

# Create your models here.
class User(models.Model):
    class Meta(object):
        db_table='user'

    name = models.CharField(
        'Name',max_length=255, null=False, blank=False
    )

    email= models.CharField(
        'Email',max_length=255, null=False, blank=False
    )

    password = models.CharField(
        'Password',max_length=255, null=False, blank=False
    )

    token= models.CharField(
        'Token',max_length=255, null=False, blank=False, db_index=True
    )

    token_expires= models.DateTimeField(
        'Token Expiration date', null=True, blank=True,
    )

    created_at=models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )

    updated_at=models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )

    def __str__(self):
        return self.email



