from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=150)
    anons = models.CharField('Анонс', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')


    def __str__(self):
        return self.title


