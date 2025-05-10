from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView


class PlacesView(TemplateView):
    template_name = 'places/places.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Малоизвестные места'
        context['content_title'] = ''
        context['content_text'] = ''

        return context
    

class FirstPlaceView(TemplateView):
    template_name = 'places/first_place.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Памятник танкистам'
        context['content_title'] = ''
        context['content_text'] = ''

        return context

class SecondPlace(TemplateView):
    template_name = 'places/second_place.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Химмашевский пруд'  
        context['content_title'] = ''
        context['content_text'] = ''

        return context
    
class ThirdPlace(TemplateView):
    template_name = 'places/third_place.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Сабуровская крепость'
        context['content_title'] = ''
        context['content_text'] = ''

        return context

class FourthPlace(TemplateView):
    template_name = 'places/fourth_place.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Река Неполодь'
        context['content_title'] = ''
        context['content_text'] = ''

        return context
    
class FifthPlace(TemplateView):
    template_name = 'places/fifth_place.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Сквер Танкистов'
        context['content_title'] = ''
        context['content_text'] = ''

        return context
    
class SixthPlace(TemplateView):
    template_name = 'places/sixth_place.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Детский парк'
        context['content_title'] = ''
        context['content_text'] = ''

        return context
    
class SeventhPlace(TemplateView):
    template_name = 'places/seventh_place.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Сквер Гуртьева'
        context['content_title'] = ''
        context['content_text'] = ''

        return context
    
class EigthPlace(TemplateView):
    template_name = 'places/eigth_place.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'ОГУ'
        context['content_title'] = ''
        context['content_text'] = ''

        return context
    
class NinethPlace(TemplateView):
    template_name = 'places/nineth_place.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)

        context['title'] = 'Памятник Ивану Грозному'
        context['content_title'] = ''
        context['content_text'] = ''

        return context

class TenthPlace(TemplateView):
    template_name = 'places/tenth_place.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Памятник Героям Гражданской Войны'
        context['content_title'] = ''
        context['content_text'] = ''

        return context

# class FirstComments(TemplateView):
#     template_name = 'places/first_comments.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         context['title'] = 'Отзывы'
#         context['content_title'] = ''
#         context['content_text'] = ''

#         return context