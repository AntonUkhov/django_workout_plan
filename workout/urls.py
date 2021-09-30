from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('powers/', views.PowerListView.as_view(), name='powers'),
    path('functionals/', views.FunctionalListView.as_view(), name='functionals'),
    path('cardios/', views.CardioListView.as_view(), name='cardios'),
    path('crossfits/', views.CrossfitListView.as_view(), name='crossfits'),
    path('pilatess/', views.PilatesListView.as_view(), name='pilatess'),
    path('rehabs/', views.RehabListView.as_view(), name='rehabs'),
    path('workout/<int:pk>', views.WorkoutDetailView.as_view(), name='workout-detail'),
    path('workout/create/', views.WorkoutCreate.as_view(), name='workout-create'),
    path('workout/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workout-update'),
    path('workout/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workout-delete'),

]

