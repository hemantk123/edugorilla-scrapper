from django.urls import path
from .views import BestsSellerFinder, SmartPhoneFinder

urlpatterns = [
    path('bestsellers/', BestsSellerFinder),
    path('smartphones/', SmartPhoneFinder),
]
