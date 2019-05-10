from django.conf.urls import url
from . import views

app_name = 'mylotto'
urlpatterns = [
        url(r'^$', views.LottoIndex, name='LottoIndex'),
]
