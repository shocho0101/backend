from django.conf.urls import url
from .views import AuthRegister, GroupList, GroupDetail, AddMember, CreateGroup
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^get-token/$',obtain_jwt_token),
    url(r'^grouplist/$',GroupList.as_view()),
    url(r'^groupdetail/(?P<id>[0-9]+)/$', GroupDetail.as_view()),
    url(r'^addmember/$',AddMember.as_view()),
    url(r'^creategroup/$',CreateGroup.as_view())
]