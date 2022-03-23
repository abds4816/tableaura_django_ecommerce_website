from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:cat_id>/', views.category, name='category'),
    path('<int:pro_id>', views.product, name='product'),
]