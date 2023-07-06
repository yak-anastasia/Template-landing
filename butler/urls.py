from django.urls import path, include
from .views import *

urlpatterns = [
    
    #path('', include('django.contrib.flatpages.urls')),
    path('', index_html, name='main'),
    path('order/', order_html, name='order'),
    path('faq/', faq_html, name='faq'),
    path('price/', price_html, name='price'),
    path('contact/', contact_html, name='contact'),
    #pages
    path('clean-car/', page_html, name='clean-car'),
    path('clean-fit/', page_html, name='clean-fit'),
    path('clean-office/', page_html, name='clean-office'),
    path('clean-tcj/', page_html, name='clean-tcj'),
    path('clean-area/', page_html, name='clean-area'),
    path('clean-facades/', page_html, name='clean-facades'),
    path('clean-apartments/', page_html, name='clean-apartments'),
    path('clean-cottages/', page_html, name='clean-cottages'),
    path('clean-out/', page_html, name='clean-out'),
    path('clean-renovation/', page_html, name='clean-renovation'),

    #path('services/<str:page>/', services_html, name="services"),
    #path('', views.flatpage, {'url': ''}, name='about'),
    #path('test/', views.flatpage, {'url': '/test/'}, name='test'),
]

