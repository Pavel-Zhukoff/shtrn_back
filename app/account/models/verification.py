from django.db import models


class VerificationModel(models.Model):
    phone = models.CharField(max_length=11, unique=True)
    code = models.CharField(max_length=8)

    class Meta:
        db_table = 'verification'