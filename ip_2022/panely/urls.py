from django.urls import path
from . import views

urlpatterns = [
    path('panely', views.panely, name='panely_pvh'),
    path('', views.pvh_bel, name='pvh_bel'),
    path('<int:pk>', views.PanelyDetailView.as_view(), name='panely_detail'),
    path('ugly', views.ugly, name='ugly'),
    path('ugly/<int:pk>', views.UgolkyDetailView.as_view(), name='ugol_detail'),
    path('complect', views.complect_pvh, name='complect_pvh'),
    path('complect/<int:pk>', views.ComplectDetailView.as_view(), name='complect_pvh_detail'),
]
