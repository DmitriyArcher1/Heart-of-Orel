"""
Конфигурация URL-адреса для проекта веб-сайта.

Список `urlpatterns` направляет URL-адреса в представления. Для получения дополнительной информации см.:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Примеры:
Представления функций
    1. Добавьте импорт: из представлений импорта my_app.
    2. Добавьте URL-адрес в urlpatterns: path('',views.home, name='home')
Представления на основе классов
    1. Добавляем импорт: fromother_app.views import Home
    2. Добавьте URL-адрес в urlpatterns: path('', Home.as_view(), name='home')
Включение другого URLconf
    1. Импортируйте функцию include(): из django.urls import include, путь
    2. Добавьте URL-адрес в urlpatterns: path('blog/', include('blog.urls'))
"""
from re import DEBUG
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace = 'main')),
    path('', include('about.urls', namespace = 'about')),
    path('places/', include('places.urls', namespace = 'places')),
    path('user/', include('users.urls', namespace = 'user')),
    path('comments/', include('comment.urls', namespace = 'comment')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)