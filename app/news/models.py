from django.db import models


class New(models.Model):
    subject = models.CharField(max_length=256, db_index=True)
    date = models.DateField(null=True, blank=True, db_index=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject
