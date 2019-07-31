from django.db import models

# Create your models here.

from django.db import models

class corpusData(models.Model):
    token = models.CharField(max_length = 100, null=False)
    token_count = models.CharField(max_length = 100, null=False)

    def __str__(self):
        return '{}'.format(self.token)