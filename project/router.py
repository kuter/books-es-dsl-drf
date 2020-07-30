from rest_framework import routers

from accounts import views as accounts_views
from books import views as book_views
from search_indexes import views as search_indexes_views

router = routers.DefaultRouter()
router.register('authors', book_views.AuthorViewSet)
router.register('books', book_views.BookViewSet)
router.register('publishers', book_views.PublisherViewSet)
router.register('tags', book_views.TagViewSet)
router.register('users', accounts_views.UserViewSet)
router.register(
    'search', search_indexes_views.BookDocumentView, basename='bookdocument'
)
