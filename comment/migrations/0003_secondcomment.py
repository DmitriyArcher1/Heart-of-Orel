from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0002_comment_avatar_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('avatar_url', models.URLField(blank=True, null=True, verbose_name='Аватар пользователя')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Комментарий второго места',
                'verbose_name_plural': 'Комментарии второго места',
                'db_table': 'second_comment',
                'ordering': ['-created_at'],
            },
        ),
    ]
