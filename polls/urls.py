from django.urls import path,re_path
from django.conf.urls import include,url
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('movies/<str:catagory>', views.movie_by_cat,name='movie_by_cat'),
    path('basket/', views.get_basket,name='get_basket'),
    path('addtobasket/<int:pk>', views.add_to_basket,name='add_to_basket'),
    path('movies/<str:catagory>/<int:pk>', views.movie_details,name='movie_details'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'),name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    
]
