from django.conf.urls import url
from DB_lms import views

urlpatterns = [
	url(r'^', views.home),
]