from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

import json
import requests

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


class URLView(View):
    """
    view: Muestra la página de inicio (index)
    """
    def dispatch(self, request, *args, **kwargs):
        """
        Llama al constructor de la clase URLView

        :param request: Solicitud
        :param args: Parametros extra
        :param kwargs: Parametros extra
        :return: Constructor de la clase Login_User
        """
        return super(URLView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            validate = URLValidator(schemes=('http', 'https', 'ftp', 'ftps', 'rtsp', 'rtmp'))
            validate(request.POST['url'])

            query_params = {
                'access_token': settings.BITLY_ACCESS_TOKEN,
                'longUrl': request.POST['url']
            }

            endpoint = 'https://api-ssl.bitly.com/v3/shorten'
            response = requests.get(endpoint, params=query_params, verify=False)

            data = response.json()

            if not data['status_code'] == 200:
                return HttpResponse(json.dumps({"code": 500, "message": "URL shortening failed!"}),
                                    content_type="application/json")
            return HttpResponse(json.dumps({"code": data['status_code'], "message": data['data']['url']}),
                                content_type="application/json")
        except ValidationError:
            return HttpResponse(json.dumps({"code": 400, "message": "Invalid URL"}), content_type="application/json")
        except:
            return HttpResponse(json.dumps({"code": 500, "message": "Process failed. Try again"}),
                                content_type="application/json")

    def get(self, request):
        session = requests.Session()  # so connections are recycled
        resp = session.head(request.GET['get_url'], allow_redirects=True)
        return HttpResponse(json.dumps({"code": 200, "message": resp.url}),
                            content_type="application/json")

