from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from petitions.views import PetitionViewSet, VoteViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'petitions', PetitionViewSet, basename='petitions')
router.register(r'votes', VoteViewSet, basename='votes')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
