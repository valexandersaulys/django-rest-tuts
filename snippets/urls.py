from django.urls import path, include
from snippets import views
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

# --> Using Router to handle ViewSet urls automatically
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# set up a CoreAPI to look at our schema -- need pyyaml too
schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
]

"""
# --> the CBV was of doing this
urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]
"""
