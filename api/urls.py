from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^add_indicators$', views.add_indicators),
    url(r'^indicators_list$', views.indicators_list)    
]
