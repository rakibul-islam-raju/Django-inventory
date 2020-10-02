from django.urls import path
from .views import (ChalanInListCreateview,
                    ChalanOutListCreateview)

app_name = 'chalan'

urlpatterns = [
    path('chalan-in/', ChalanInListCreateview.as_view(), name='chalan-in'),
    path('chalan-out/', ChalanOutListCreateview.as_view(), name='chalan-out'),
]
