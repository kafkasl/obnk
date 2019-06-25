# Django Rest Framewok
from django.conf.urls import url

# obnk
from views import Login, SignUp, OwnUserProfile, UserProfile


urlpatterns = [
    url(r'^signup/$', SignUp.as_view()),
    url(r'^login/$', Login.as_view()),
    url(r'^profiles/$', OwnUserProfile.as_view()),
    url(r'^profiles/(?P<user_uuid>[0-9a-z-]+)/$', UserProfile.as_view()),
]
