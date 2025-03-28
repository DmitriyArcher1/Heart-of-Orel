from django.db import models

from users.models import User

class Comment(models.Model):
    text = models.TextField(verbose_name = 'Комментарий')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')

    class Meta:
        db_table = 'comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Комментарий от - {self.author}"