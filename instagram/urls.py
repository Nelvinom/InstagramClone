from django.conf.urls.static import static
from django.conf.urls import url
from .import views


urlpatterns=[
    url(r'^$', views.instagram, name='instagram'),
    url(r'^search/', views.search_results, name='search_results'),
]