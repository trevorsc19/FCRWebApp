"""VRWare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from api.views import PersonList
from api.views import PersonDetail
from api.views import delete_table

"""
docs.djangoproject.com/en/2.2/topics/urls - How Django processes a request, path converters, custom path converters (class and regular expressions)
"""

# pk will be the name of the parameter passed to the get() method. We can name this whatever we want.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/people/', PersonList.as_view()),
    path('api/people/<int:pk>', PersonDetail.as_view()),
    path('deletetable/', delete_table),
    path('api/people/<int:pk>', PersonDetail.as_view()),
]