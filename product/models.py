from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class Category(models.TextChoices):
    ACTIVITY = "activity"
    BUSINESS_AND_FINANCE = "business and finance"
    EDUCATIONAL_RESOURCES = "educational resources"
    ENTERTAINMENT = "entertainment"
    HEALTHCARE = "healthcare"
    HOME_IMPROVEMENT = "home improvement"
    INDUSTRY_NEWS = "industry news"
    LIFESTYLE = "lifestyle"
    NEWS = "news"
    POLITICS = "politics"
    RELIGION = "religion"
    SCIENCE = "science"
    SPORTS = "sports"
    TECHNOLOGY = "technology"
    TRAVEL = "travel"
    WORLD = "world"
    

class Product(models.Model):
    name = models.CharField(max_length=120, default='',blank=False)
    price = models.FloatField(default=0)
    description = models.TextField(max_length=200, blank=False)
    rate = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=50, default='', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=Category.choices)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5, "The maximum rating value is 5.")]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.user.username} on {self.product.name}"