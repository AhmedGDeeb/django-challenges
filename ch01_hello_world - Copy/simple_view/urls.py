from django.urls import path
from .views import index, HelloPageView, HelloUserPageView


urlpatterns = [
    # from views
    path("", index, name="hello_view"),

    # from template
    path('from_template/', HelloPageView.as_view(), name='hello_template'),
    
    # add usre name
    path('from_template/<str:user_name>', HelloUserPageView.as_view(), name='hello_user'),
]
