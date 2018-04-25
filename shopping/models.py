from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image_name = models.CharField(max_length=200)

    SkinCare = "SC"
    Powders = "PR"
    Scrubs = "SB"

    categories = (
        (SkinCare, "Skin Care"),
        (Powders, "Powders"),
        (Scrubs, "Scrubs"),
    )
    category = models.CharField(
        max_length=10,
        choices=categories,
        default=SkinCare
    )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Products"

class Reviews(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    stars = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Reviews"




