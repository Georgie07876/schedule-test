from django.urls import path, include
 
urlpatterns = [
    path("schedule/", include("api.v1.schedule.urls")),
]