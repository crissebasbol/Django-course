from django.urls import path, re_path

from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        "personas/",
        views.ListPersonaListView.as_view(),
        name="personas"
    ),
    path(
        "api/person/list/",
        views.PersonListAPIView.as_view(),
    ),
    path(
        "list",
        views.PersonListView.as_view(),
        name="list"
    ),
    path(
        "api/person/search/<kword>/",
        views.PersonSearchAPIView.as_view(),
    )
]