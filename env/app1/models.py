from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name
