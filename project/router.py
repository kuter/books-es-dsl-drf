from rest_framework import routers

from accounts import views as accounts_views
from books import views as book_views

router = routers.DefaultRouter()
router.register('books', book_views.BookViewSet)
router.register('users', accounts_views.UserViewSet)
