from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset',views.BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('get', views.getBook), 
    path('book/', views.BookView.as_view()), #GET POST PUT PATCH Delete
    path('register/',views.UserView.as_view()),
    path('genericBook/',views.BookGeneric.as_view()),
    path('genericUser/',views.UserGeneric.as_view()),
    path('genericUserModify/<int:pk>',views.UserGenericModify.as_view()),
    path('pdf/',views.GeneratePdf.as_view()),
    path('user/',views.UserSerializer),
]



