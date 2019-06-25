# Django Rest Framewok
# from rest_framework.routers import DefaultRouter
#
# # twins
# from views import TransfersViewSet
#
# router = DefaultRouter()
# url(r'^signup/$', SignUp.as_view()),
#
# router.register(r'transfers', TransfersViewSet,
#                 base_name="Transfer")
# urlpatterns = router.urls

# Django Rest Framewok
from django.conf.urls import url

# obnk
from views import Transfers


urlpatterns = [
    url(r'^transfers/$', Transfers.as_view()),
]
