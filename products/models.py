from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'menu'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'


class Drink(models.Model):
    name = models.CharField(max_length=45)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergy'

class AllergyDrink(models.Model):
    allergy_id = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    drink_id = models.ForeignKey(Drink, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'allergy_drink'

class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

    class Meta:
        db_table = 'size'


class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2)
    staturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2)
    drink_id = models.ForeignKey(Drink, on_delete=models.CASCADE)
    size_id = models.ForeignKey(Size, on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutrition'


class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink_id = models.ForeignKey(Drink, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'


        