"""chider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,include
from django.contrib.auth import views as v
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/',v.LoginView.as_view(),name='login'),
    path('accounts/logout/',v.LogoutView.as_view(), name='logout'),
    path('',views.dashboard,name='dashboard'),
    path('screen',views.screen_page,name='home'),
    #dates
    path('calendar/',views.MyDateListView.as_view(),name='calendar'),
    path('new/',views.CreateMyDateView.as_view(),name='mydate_new'),
    path('date/<int:pk>',views.my_date_detail,name='date_detail'),
    path('date/<int:pk>/edit/',views.MyDateUpdateView.as_view(),name='date_edit'),
    path('date/<int:pk>/delete/',views.MyDateDeleteView.as_view(),name='date_delete'),
    path('date/<int:pk>/preview/',views.day_preview,name='preview'),
    #images
    path('images/',views.ImagesListView.as_view(),name='images'),
    path('import_images/',views.create_image_view,name='import_images'),
    path('image/<int:pk>/delete/',views.ImagesDeleteView.as_view(),name='image_delete'),
    #image to date
    path('date/<int:pk>/add_image/',views.create_day_image_view,name='add_image'),
    path('dayimage/<int:pk>/',views.DayImageDetailView.as_view(),name='dayimage_detail'),
    path('dayimage/<int:pk>/delete/',views.day_image_delete,name='dayimage_delete'),
    #mazel
    path('date/<int:pk>/add_mazel/',views.create_mazel_tov,name='add_mazel'),
    path('mazel/<int:pk>/',views.MazelTovDetailView.as_view(),name='mazel_detail'),
    path('mazel/<int:pk>/edit_mazel/',views.MazelTovUpdateView.as_view(),name='edit_mazel'),
    path('mazel/<int:pk>/delete/',views.mazel_tov_delete,name='mazel_delete'),
    #massage
    path('message/<int:pk>/edit_message/',views.MessageUpdateView.as_view(),name='edit_message'),
    #add
    path('add/',views.AddCreateView.as_view(),name='add'),
    #login
    path('accounts/profile/',views.LoginRedirect.as_view(),name='login_redirect'),
    path('/accounts/logout/',views.LogoutRedirect.as_view(),name='logout_redirect'),
]+ staticfiles_urlpatterns()




if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
