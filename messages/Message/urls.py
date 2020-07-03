from django.urls import path
from . import views

app_name = 'messages'

urlpatterns = [
    path('new/',views.CreateMessage.as_view(),name='create_message'),
    path('all/',views.MessageList.as_view(),name='all'),
    path('profile/<username>/<int:pk>/',views.MessageDetail.as_view(),name='users'),
    path('profile/<int:pk>/delete/',views.MessageDelete.as_view(),name='delete'),
    path('<username>/',views.UserMessages.as_view(),name='user'),
]