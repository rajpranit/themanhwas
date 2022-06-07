from django.urls import path 
from . import views

urlpatterns = [

    path('',views.index,name='index'),


    # path('top-article/<int:pk>',views.top_article,name='top-article'),
    # path('manhua-article/<int:pk>',views.manhua_article,name='manhua-article'),
    # path('manhwa-article/<int:pk>',views.manhwa_article,name='manhwa-article'),

    path('article-detail/<int:pk>',views.article_detail,name='article-detail'),
    path('comment/<int:pk>',views.comment,name='comment'),

    path('search_content',views.search_content,name='search_content'),

    path('category',views.category,name='category'),
    
    path('category/manhwa',views.manhwa,name='manhwa'),
    path('category/manhua',views.manhua,name='manhua'),


    path('about/',views.about,name='about'),
    path('contact',views.contact,name='contact'),



]