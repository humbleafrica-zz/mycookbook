from __future__ import unicode_literals

from django.conf import settings
from django.utils import timezone
from django.db import models
from django.conf.urls import include, url
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.

        
#recipe model

user = User

class Recipe(models.Model):
     #meal choices
    BREAKFAST ="BREAKFAST"
    LUNCH = "LUNCH"
    DINNER = "DINNER"
    DESSERT = "DESSERT"
    STARTER = "STARTER"
    BRUNCH = "BRUNCH"
    SNACK = "SNACK"
    MAIN = "MAIN"
    SIDE = "SIDE"
    DRINK = "DRINK"
    COCKTAIL = "COCKTAIL"
    CANAPE = "CANAPE"
    
    RECIPE_TYPE_CHOICES =(
         (BREAKFAST,"BREAKFAST"),
         (LUNCH,"LUNCH"),
         (DINNER,"DINNER"),
         (STARTER,"STARTER"),
         (DESSERT,"DESSERT"),
         (BRUNCH, "BRUNCH"),
         (SNACK, "SNACK"),
         (MAIN, "MAIN COURSE"),
         (SIDE, "SIDE DISH"),
         (DRINK, "DRINK"),
         (COCKTAIL, "COCKTAIL"),
         (CANAPE, "CANAPE"),
        )
    
    #difficulty choices
    NOVICE ="EASY"
    ADV_BEGINNER = "NORM"
    COMPETENT = "HARD"
    EXPERT ="EXPERT"
    
    DIFF_TYPE_CHOICES =(
        (NOVICE, "EASY"),
        (ADV_BEGINNER, "NORMAL"),
        (COMPETENT, "HARD"),
        (EXPERT, "EXPERT"),
        )
    
    #publisher choices
    MAGAZINE = "MAGAZINE"
    NEWSPAPER = "NEWSPAPER"
    WEBSITE = "WEBSITE"
    BOOK = "BOOK"
    SOCIAL_CLUB = "SOCIAL CLUB"
    PROFESSIONAL = "PROFESSIONAL"
    
    PUBLISHER_CHOICE =(
        (MAGAZINE, "MAGAZINE"),
        (NEWSPAPER, "NEWSPAPER"),
        (WEBSITE, "WEBSITE"),
        (BOOK, "BOOK"),
        (SOCIAL_CLUB, "SOCIAL CLUB"),
        (PROFESSIONAL, "PROFESSIONAL"),
        )
    
    #allergy warnings
    NONE = "NONE"
    MILK = "MILK"
    EGG = "EGG"
    NUT = "NUT"
    SOYA = "SOYA"
    WHEAT = "WHEAT"
    FISH = "FISH"
    PORK = "PORK"
    ALERGY_CHOICE =(
        (NONE, "NONE"),
        (MILK, "MILK"),
        (EGG, "EGG"),
        (NUT, "NUT"),
        (SOYA, "SOYA"),
        (WHEAT, "WHEAT"),
        (FISH, "FISH"),
        (PORK, "PORK"),
        )
        
    #cuisine type
    
    AFRICAN = "AFRICAN"
    AMERICAN = "AMERICAN"
    ASIAN ="ASIAN"
    AUSTRALIAN = "AUSTRALIAN"
    EUROPEAN = "EUROPEAN"
    CARIBBEAN = "CARIBBEAN"
    MEDITERRANEAN ="MEDITERRANEAN"
    
    CUISINE_CHOICE =( 
        ("AFRICAN", "AFRICAN"),
        ("AMERICAN", "AMERICAN"),
        ("ASIAN", "ASIAN"),
        ("AUSTRALIAN", "AUSTRALIAN"),
        ("CARIBBEAN", "CARIBBEAN"),
        ("EUROPEAN", "EUROPEAN"),
        ("MEDITERRANEAN", "MEDITERRANEAN"),
        )
    
     # DATABASE FIELDS
    recipe_name = models.CharField(max_length=200)
    serves = models.IntegerField()
    scalable = models.BooleanField(default=True)
    prep_time = models.IntegerField("Prep Min")
    cook_time = models.IntegerField("Cook Min")
    description = models.TextField(max_length=4000)
    ingredients = models.TextField(max_length=1500)
    method = models.TextField(max_length=15000)
    publisher = models.CharField("publisher", max_length = 20, choices = PUBLISHER_CHOICE)
    allergy = models.CharField("allergy", max_length = 20, choices = ALERGY_CHOICE)
    difficulty = models.CharField("difficulty", max_length = 10, choices = DIFF_TYPE_CHOICES)
    recipe_type = models.CharField("recipe Type", max_length = 20, choices = RECIPE_TYPE_CHOICES)
    cuisine = models.CharField("cuisine", max_length = 20, choices = CUISINE_CHOICE)
    uploaded_date = models.DateField(("Date Uploaded"), auto_now=False, auto_now_add=True)
    updated = models.DateField(("Last Updated"), auto_now=True,auto_now_add=False)
    image = models.ImageField(upload_to="recipes/",)
    notes = models.TextField(max_length=1500, blank=True)
    country = models.CharField(max_length=50)
    author = models.CharField(max_length=50, blank = False)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")

    def __str__(self):
        self.save()
        return self.recipe_name
    # meta class
    class Meta:
        verbose_name = "recipe"
        verbose_name_plural = "recipes"
    
    # to string method
    def total_likes(self):
        return self.likes.count()
        
    # absolute url method
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})