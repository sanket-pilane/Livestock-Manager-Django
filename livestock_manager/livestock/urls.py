
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('livestock/add/', views.LivestockCreateView.as_view(), name='livestock_add'),
    path('livestock/<int:pk>/edit/', views.LivestockUpdateView.as_view(), name='livestock_edit'),
    path('livestock/<int:pk>/delete/', views.LivestockDeleteView.as_view(), name='livestock_delete'),
]
