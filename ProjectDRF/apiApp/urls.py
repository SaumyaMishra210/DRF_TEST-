from django.urls import path 
from . import views


urlpatterns = [
    path('', views.BookView.as_view()), #GET POST
    path('book/', views.BookView.as_view()), #PUT PATCH Delete
    path('register/',views.UserView.as_view()),
    path('genericBook/',views.BookGeneric.as_view()),
    path('genericUser/',views.UserGeneric.as_view()),
    path('genericUserModify/<int:pk>',views.UserGenericModify.as_view()),
    path('pdf/',views.GeneratePdf.as_view()),
    path('user/',views.UserSerializer),
]



