"""
URL configuration for cpce_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    #URLS Administration appli
    path('admin/', admin.site.urls),
    
    # #URL Authentification
    # path('accounts/register/', views.register_page, name='register'),
    # # path('profile<int:id>/', views.profile, name='profile'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/profile/', views.profile, name='profile'),

    # #URLS economic_exchanges
    # path('home/', views.dashboard, name='dashboard'),

    # path('product/', views.product_home),
    # path('product/<int:id>/', views.product_detail, name='product-detail'),

    # path('producer/', views.producer_home, name='producer-list'),
    # path('producer/<int:id>/', views.producer_detail, name='producer-detail'),

    # path('supplier/', views.supplier_home, name='supplier-list'),
    # path('supplier/<int:id>/', views.supplier_detail, name='supplier-detail'),
    # path('supplier/add/', views.supplier_create, name='supplier-create'),

    # path('client/', views.client_home),
    # path('client/comp<int:id>/', views.client_company_detail, name='client-company-detail'),
    # path('client/pers<int:id>/', views.client_personal_detail, name='client-personal-detail'),

    # path('declaration/', views.declaration_home),
    # path('declaration/purch<int:id>/', views.declaration_purchase_detail, name='declaration-purchase-detail'),
    # path('declaration/sal<int:id>/', views.declaration_sale_detail, name='declaration-sale-detail'),

    # path('contact/', views.contact, name='contact'),
    # path('contact-sent/', views.contact_sent, name='contact-sent'),
    
    # #Others pages
    # path('faq/', views.page_faq, name='faq'),
]
