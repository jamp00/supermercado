from django.urls import path

from apps.plot.views import home, plotS1

urlpatterns = [
    path('home/', home),
    path('plotS1/', plotS1),
]
