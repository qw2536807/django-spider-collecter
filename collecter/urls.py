from django.urls import include, path
from rest_framework import routers
# from collecter import views


from collecter.Apiview import RecodeView
from collecter.Apiview import MetadataView


router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    path("Recode/", RecodeView.RecodeView.as_view()),
    path("Metadata/", MetadataView.MetadataView.as_view()),
]
