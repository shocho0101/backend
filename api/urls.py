from django.conf.urls import url
from .views import AuthRegister
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^get-token/$',obtain_jwt_token)
]