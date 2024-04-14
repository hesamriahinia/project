from django.urls import path
from hesam.views import home, blog, info
urlpatterns = [
    path('', home),
    path('blog', blog),
    path('info', info)
]
