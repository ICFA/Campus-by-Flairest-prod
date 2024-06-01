from django.urls import path
from flairest_campus import views
from flairest_campus.models import LogMessage


urlpatterns = [
    path('', views.home_page),
    path('profile/', views.profile_page, name='profile'),
    path('catalog/', views.UniCatalog, name='catalog'),
    path('unicreate/', views.UniAdd.as_view(), name="add_uni"),
    path('catalog/uni/<int:uni_id>/', views.uni_detail, name='curr_uni'),
    path('edit/<int:pk>/', views.UniEdit.as_view(), name='edit_uni'),
    path('speccreate/', views.SpecAdd.as_view(), name="add_spec"),
    path('catalog/spec/<int:spec_id>/', views.spec_detail, name='curr_spec'),
    path('specedit/<int:pk>/', views.SpecEdit.as_view(), name='edit_spec')
]