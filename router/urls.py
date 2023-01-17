from django.urls import path
from . import views
from .views import URLListView

urlpatterns = [
    path('', views.home, name='home'),
    path('how-to/', views.how_to, name='how-to'),
    path('shortened-urls/', URLListView.as_view(), name='url-list'),
    path('<slug:key>/', views.redirector, name='redirector')
]