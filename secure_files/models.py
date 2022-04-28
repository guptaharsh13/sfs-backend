from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class File(models.Model):
    file = models.FileField(verbose_name="File")
    user = models.ForeignKey(verbose_name="Author",
                             to=User, on_delete=models.DO_NOTHING)
