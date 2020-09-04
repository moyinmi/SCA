from django.urls import path
from .views import HomePage, ReadM, CreateArticle

app_name ="articles"


urlpatterns = [
    path('', HomePage.as_view(), name ="HomePage"),
    path('create/', CreateArticle.as_view(success_url='/'), name="CreateArticle"),
    path('detail/<int:pk>/', ReadM.as_view(), name = "detail-view"),
]
