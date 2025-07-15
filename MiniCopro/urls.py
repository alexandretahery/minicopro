from django.urls import path
from MiniCopro.views import MiniApi
urlpatterns = [
    path("", MiniApi, name="dashboard.html"),
]
