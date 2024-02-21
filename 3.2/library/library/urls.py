"""
URL configuration for library project.

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
from rest_framework.routers import SimpleRouter

from main.views import (books_list, CreateBookView, BookDetailsView, BookUpdateView,
                        BookDeleteView, OrderViewSet)

router = SimpleRouter()
#зарегистрируйте вьюсет для заказов


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', books_list),
    path('api/v1/books/create/', CreateBookView.as_view()),
    path('api/v1/books/<int:pk>/', BookDetailsView.as_view()),
    path('api/v1/books/update/<int:pk>/', BookUpdateView.as_view()),
    path('api/v1/books/delete/<int:pk>/', BookDeleteView.as_view()),
    path("api/v1/", include(router.urls))
]
