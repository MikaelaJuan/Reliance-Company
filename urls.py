
from django.contrib import admin
from django.urls import path, include

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee_register.urls')),
    path('accounts/', include('allauth.urls')),

]
