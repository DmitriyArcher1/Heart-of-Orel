from tabnanny import verbose
from django.db import models
from django.template.defaulttags import verbatim

from users.models import User

class Comment(models.Model):
    text = models.TextField(verbose_name = 'Комментарий')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    avatar_url = models.URLField(blank = True, null = True, verbose_name = 'Аватар пользователя')

    def save(self, *args, **kwargs):
        if self.author.image:
            self.avatar_url = self.author.image.url
            
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Комментарий от - {self.author}"

class SecondComment(models.Model):
    text = models.TextField(verbose_name = 'Комментарий')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    avatar_url = models.URLField(blank = True, null = True, verbose_name = 'Аватар пользователя')

    def save(self, *args, **kwargs):
        if self.author.image:
            self.avatar_url = self.author.image.url
        
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'second_comment'
        verbose_name = 'Комментарий второго места'
        verbose_name_plural = 'Комментарии второго места'
        ordering = ['-created_at']

    def __str__(self):
        return f"Комментарий от - {self.author}"
    
class ThirdComment(models.Model):
    text = models.TextField(verbose_name = 'Комментарий')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    avatar_url = models.URLField(blank = True, null = True, verbose_name = 'Аватар пользователя')

    def save(self, *args, **kwargs):
        if self.author.image:
            self.avatar_url = self.author.image.url
        
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'third_comment'
        verbose_name = 'Комментарий третьего места'
        verbose_name_plural = 'Комментарии третьего места'
        ordering = ['-created_at']

    def __str__(self):
        return f"Комментарий от - {self.author}"
    
class FourthComment(models.Model):
    text = models.TextField(verbose_name = 'Комментарий')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    avatar_url = models.URLField(blank = True, null = True, verbose_name = 'Аватар пользователя')

    def save(self, *args, **kwargs):
        if self.author.image:
            self.avatar_url = self.author.image.url
        
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'fourth_comment'
        verbose_name = 'Комментарий четвёртого места'
        verbose_name_plural = 'Комментарии четвёртого места'
        ordering = ['-created_at']

    def __str__(self):
        return f"Комментарий от - {self.author}"


class FifthComment(models.Model):
    text = models.TextField(verbose_name = 'Комментарий')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    avatar_url = models.URLField(blank = True, null = True, verbose_name = 'Аватар пользователя')

    def save(self, *args, **kwargs):
        if self.author.image:
            self.avatar_url = self.author.image.url
        
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'fifth_comment'
        verbose_name = 'Комментарий пятого места'
        verbose_name_plural = 'Комментарии пятого места'
        ordering = ['-created_at']

    def __str__(self):
        return f"Комментарий от - {self.author}"
    
class SixthComment(models.Model):
    text = models.TextField(verbose_name = 'Комментарий')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    avatar_url = models.URLField(blank = True, null = True, verbose_name = 'Аватар пользователя')

    def save(self, *args, **kwargs):
        if self.author.image:
            self.avatar_url = self.author.image.url
        
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'sixth_comment'
        verbose_name = 'Комментарий шестого места'
        verbose_name_plural = 'Комментарии шестого места'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Комментарий от - {self.author}"
    
class SeventhComment(models.Model):
    text = models.TextField(verbose_name = 'Комментарий')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    avatar_url = models.URLField(blank = True, null = True, verbose_name = 'Аватар пользователя')

    def save(self, *args, **kwargs):
        if self.author.image:
            self.avatar_url = self.author.image.url

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'seventh_comment'
        verbose_name = 'Комментарий седьмого места'
        verbose_name_plural = 'Комментарии седьмого места'
        ordering = ['-created_at']

    def __str__(self):
        return f"Комментарий от - {self.author}"
    
class EigthComment(models.Model):
    text = models.TextField(verbose_name = 'Комментарий')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    avatar_url = models.URLField(blank = True, null = True, verbose_name = 'Аватар пользователя')

    def save(self, *args, **kwargs):
        if self.author.image:
            self.avatar_url = self.author.image.url
        
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'eigth_comment'
        verbose_name = 'Комментарий восьмого места'
        verbose_name_plural = 'Комменатрии восьмого места'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Комменатарий от - {self.author}"

class NinethComment(models.Model):
    text = models.TextField(verbose_name = 'Комментарий')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    avatar_url = models.URLField(blank = True, null = True, verbose_name = 'Аватар пользователя')

    def save(self, *args, **kwargs):
        if self.author.image:
            self.avatar_url = self.author.image.url
        
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'nineth_comment'
        verbose_name = 'Комментарий девятого места'
        verbose_name_plural = 'Комментарии девятого места'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Комментарий от - {self.author}"

class TenthComment(models.Model):
    text = models.TextField(verbose_name = 'Комментарий')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    avatar_url = models.URLField(blank = True, null = True, verbose_name = 'Аватар пользователя')

    def save(self, *args, **kwargs):
        if self.author.image:
            self.avatar_url = self.author.image.url
        
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'tenth_comment'
        verbose_name = 'Комментарий десятого места'
        verbose_name_plural = 'Комментарии десятого места'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Комментарий от - {self.author}"