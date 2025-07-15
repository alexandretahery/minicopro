from django.urls import path
from MiniCopro.views import stats_view

urlpatterns = [
    path("dashboard/", stats_view, name="dashboard"),
]
