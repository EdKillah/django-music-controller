from django.urls import path
from .views import main, RoomView

urlpatterns = [    
    path('', main),
    path('room',RoomView.as_view())
]
