from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('chat/', views.chat_with_ai, name='chat_with_ai'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('index/', views.index, name='index'),  # ✅ Index page endpoint
    # path('chat/', views.chat_with_ai, name='chat_with_ai'),  # ✅ Chat with AI endpoint
]
