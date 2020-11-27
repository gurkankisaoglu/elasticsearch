from django.conf.urls import url, include

from .views import TaskDocumentView
from django.urls import path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
books = router.register(r'tasks',
                        TaskDocumentView,
                        basename='taskdocument')

urlpatterns = [
    url(r'^', include(router.urls)),
]