from django.urls import path
from .views import chatbot_response

urlpatterns = [
    path('chat/', chatbot_response, name='chatbot_response'),  # Exposes /chat/ endpoint
]