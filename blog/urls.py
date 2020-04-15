from django.urls import path

from blog import views

urlpatterns = [
                  path(r'reg/', views.register, name='reg'),
                  path(r'login/', views.login_view, name='login'),
                  path(r'index/', views.index, name='index'),
              ]






