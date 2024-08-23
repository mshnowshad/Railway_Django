from django.db import models

# Create your models here.


class Names_app(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/projects/', blank=False, null=True)
    def __str__(self):
        return self.name