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
    template_name = 'first_place.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Памятник танкистам'
        context['content_title'] = ''
        context['content_text'] = ''

        return context