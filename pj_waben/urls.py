"""pj_waben URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from waben import views
from django.contrib.auth.decorators import login_required

index_view = views.IndexView.as_view()

urlpatterns = [
    path('detai/',views.DetaiView.as_view(),name='detai'),
    path('total/',views.TotalView.as_view(),name='total'),
    path('fix/',views.FixView.as_view(),name="fix"),
    path('fix2/',views.Fix2View.as_view(),name="fix2"),
    path('check/',views.CheckView.as_view(),name="check"),
    path('check2/',views.Check2View.as_view(),name="check2"),
    path('next/',views.NextView.as_view(),name="next"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path("", login_required(index_view), name="index"),
    path('', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
]
