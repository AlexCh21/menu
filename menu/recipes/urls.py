from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('calculator/', include('calculator.urls')),
]
