from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^url/', views.URLView.as_view(), name='url')
]
