from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class ButlerPage(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Простая страница'
        verbose_name_plural = 'Простые страницы'
    
class FAQmodel(models.Model):
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.question
    
    class Meta:
        verbose_name = 'FAQ'