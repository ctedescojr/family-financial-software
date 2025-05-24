from django.urls import path
from .views import about

app_name = "expenses"
urlpatterns = [path("about/", about, name="about")]
