from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class EnglishWord(models.Model):
    word = models.CharField(max_length=255)
    rus_translation = models.ManyToManyField("RussianWord", through="Picture", related_name="related_russian")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word

class RussianWord(models.Model):
    word = models.CharField(max_length=255)
    eng_translation = models.ManyToManyField("EnglishWord", through="Picture", related_name="related_english")

    def __str__(self):
        return self.word

class Picture(models.Model):
    image = models.FileField(blank=True, null=True)
    desctiption = models.TextField(blank=True, null=True)
    english_word = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)
    russian_word = models.ForeignKey(RussianWord, on_delete=models.CASCADE)


