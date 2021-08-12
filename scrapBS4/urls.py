from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('word-dictionary', views.wordDictionary, name='word-dictionary'),
    # path('search',views.searchWord, name='search-word').
    path('meta-generator', views.metaGenerator, name='meta-generator'), 
    path('text-generator', views.textGenerator, name='text-generator'),
    path('blog-pdf/', views.getPdf, name="get-pdf"),
    path('blog', views.Blog, name="blog"),
    # path('<str:slug>', views.BlogPost, name="blogpost"),
    path('price-tracker', views.priceTracker, name='price-tracker'),
    path('delete/<pk>/', views.LinkDeleteView.as_view(), name="delete"),
    path('update', views.update_prices, name="update-prices"),
  
]

