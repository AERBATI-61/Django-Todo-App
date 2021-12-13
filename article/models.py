from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Baslik")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Tarih")
    article_image = models.FileField(blank=True, null=True, verbose_name="Makaleye fotograf veya dosya ekleyin")
    is_home = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_date"]


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name='comments')
    comment_author = models.CharField(max_length=50, verbose_name="isim")
    comment_content = RichTextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_author

    class Meta:
        ordering = ["-comment_date"]


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
