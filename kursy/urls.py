from django.urls import path
from kursy.views import (
    KursListCreateView, KursRetrieveUpdateDestroyView,
    LekcjaListCreateView, LekcjaRetrieveUpdateDestroyView,
    AutorListCreateView, KursStatsView
)

urlpatterns = [
    path('kursy/', KursListCreateView.as_view()),
    path('kursy/<int:pk>/', KursRetrieveUpdateDestroyView.as_view()),
    path('kursy/statystyki/', KursStatsView.as_view()),
    path('lekcje/', LekcjaListCreateView.as_view()),
    path('lekcje/<int:pk>/', LekcjaRetrieveUpdateDestroyView.as_view()),
    path('autorzy/', AutorListCreateView.as_view()),
]
