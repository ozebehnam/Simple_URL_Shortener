from django.urls import path, include
from .import views
from .views import URLListView, SignUpView

urlpatterns = [
    path('', views.home, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path('how-to/', views.how_to, name='how-to'),
    path('shortened-urls/', URLListView.as_view(), name='url-list'),
    path('accounts/logout/',views.home, name='sign-out'),
    path('<slug:key>/', views.redirector, name='redirector'),
]