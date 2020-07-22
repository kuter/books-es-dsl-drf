from rest_framework import routers

from accounts import views as accounts_views
from books import views as book_views
from search_indexes import views as search_indexes_views

router = routers.DefaultRouter()
router.register('books', book_views.BookViewSet)
router.register('users', accounts_views.UserViewSet)
router.register(
    'search', search_indexes_views.BookDocumentView, basename='bookdocument'
)
