from django.db import models

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
