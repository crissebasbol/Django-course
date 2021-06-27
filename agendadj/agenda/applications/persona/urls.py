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
        "api/persona/list",
        views.PersonListAPIView.as_view(),
    )
]