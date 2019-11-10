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
from django.urls import path
from profile.views import PersonList
from profile.views import PersonDetail
from profile.views import delete_table
from profile.views import test_404_handler
from profile.views import upload_document
from profile.views import upload_image


"""
docs.djangoproject.com/en/2.2/topics/urls - How Django processes a request, path converters, custom path converters (class and regular expressions)
"""

# pk will be the name of the parameter passed to the get() method. We can name this whatever we want.
urlpatterns = [
    path('profile/people/', PersonList.as_view()),
    path('profile/people/<int:pk>', PersonDetail.as_view()),
    path('deletetable/', delete_table),
    path('profile/people/<int:pk>', PersonDetail.as_view()),
    path('profile/404_error_test', test_404_handler),
    path('profile/upload_doc', upload_document), 
    path('profile/upload_image', upload_image),
]

# DEBUG must be set to 'False' in settings.py for this to work
handler404='profile.views.handle_404_method'