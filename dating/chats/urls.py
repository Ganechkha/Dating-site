from django.urls import path

from . import views


app_name = 'chats'

urlpatterns = [
    path('', views.ChatsListView.as_view(),
         name='chats_list'),
    path('create/', views.CreateChatView.as_view(),
         name='create_chat'),
    path('<str:chat_id>/',
         views.ChatConnectDetailView.as_view(),
         name='chat_connect')
]