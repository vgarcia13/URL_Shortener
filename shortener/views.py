from django.shortcuts import render, redirect
from django.views.generic import View

__author__ = 'vgarcia13'


class IndexView(View):
    """
    view: Muestra la página de inicio (index)
    """
    def dispatch(self, request, *args, **kwargs):
        """
        Llama al constructor de la clase IndexView

        :param request: Solicitud
        :param args: Parametros extra
        :param kwargs: Parametros extra
        :return: Constructor de la clase Login_User
        """
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        """
        Verifica una sesión ya este activa y permite el acceso o la deniega.

        :param request: Solicitud
        :return: Redirige a la vista pertinente
        """
        return render(request, 'shortener/index.html')