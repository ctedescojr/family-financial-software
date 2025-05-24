from django.urls import path
from .views import upload_invoice

app_name = "shopping"
urlpatterns = [path("upload_invoice/", upload_invoice, name="upload_invoice")]
