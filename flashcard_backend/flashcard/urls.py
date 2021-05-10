from django.urls import path
from . import views

urlpatterns = [
    path('flashcard/', views.FlashcardList.as_view()),
    path('flashcard/<int:fk>/', views.FlashcardDetail.as_view()),
    path('flashcard/<int:pk>/', views.PutPath.as_view()),
]