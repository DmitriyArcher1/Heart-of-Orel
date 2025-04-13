from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='avatar_url',
            field=models.URLField(blank=True, null=True, verbose_name='Аватар пользователя'),
        ),
    ]
