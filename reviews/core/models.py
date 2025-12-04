from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class ReviewModel(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    review=models.TextField()
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])