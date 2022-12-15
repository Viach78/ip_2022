from django.urls import path
from . import views

urlpatterns = [
    path('catalog/krasky', views.krasky, name='krasky'),
    path('krasky', views.krasky, name='krasky'),
    path('krasky/krasky_vd', views.krasky_vd, name='krasky_vd'),
    path('krasky_vd/krasky_vnut', views.krasky_vnut, name='krasky_vnut'),
    path('<int:pk>', views.KraskyvnutDetailView.as_view(), name='krasky_vnut_detail'),
    path('krasky_vd/krasky_nar', views.krasky_nar, name='krasky_nar'),
    path('krasky_nar/<int:pk>', views.KraskynarDetailView.as_view(), name='krasky_nar_detail'),
    path('krasky/krasky_pf', views.krasky_pf, name='krasky_pf'),
    path('krasky_aero', views.krasky_aero, name="krasky_aero"),
    path('krasky_aero/<int:pk>', views.KraskyaeroDetailView.as_view(), name='krasky_aero_detail'),
    path('krasky_rust', views.krasky_rust, name="krasky_rust"),
    path('krasky_rust/<int:pk>', views.KraskyrustDetailView.as_view(), name='krasky_rust_detail'),
]