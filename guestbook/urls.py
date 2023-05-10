from django.urls import path
from guestbook.views import *

urlpatterns = [
    path("<int:id>", get_or_delete_GuestBook, name = 'get_or_delete_GuestBook'),
    path("", create_or_getAll_GuestBook, name = 'create_or_getAll_GuestBook'),
]