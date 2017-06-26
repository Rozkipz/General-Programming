from django.db import models

# Create your models here.
class Document(models.Model):
    Document = models.FileField(upload_to='')