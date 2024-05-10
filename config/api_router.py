from django.urls.conf import include, path
from graphene_django.views import GraphQLView

app_name = "api"
urlpatterns = (
    path("users/", include("api_project.users.urls")),
    path("graphql", GraphQLView.as_view(graphiql=True)),
)
