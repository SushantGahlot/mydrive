from django.db import models
import os


# Create your models here.

class File(models.Model):
    category_choices = (
        ('Financial Document', 'Financial Document'),
        ('Marketing Document', 'Marketing Document'),
        ('Technical Document', 'Technical Document')
    )

    category = models.CharField(max_length=20, choices=category_choices)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=100)

    # because django adds media path to files to make them easily accessible, we need a
    # field just to save the filename to query on it
    def save(self, *args, **kwargs):
        self.filename = os.path.basename(self.file.name)
        super(File, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-uploaded_at']
