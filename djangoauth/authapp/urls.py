from django.conf.urls import url
from views import home_view, login_view, create_user_view

urlpatterns = [
    url('^createuser/$', create_user_view),
]
