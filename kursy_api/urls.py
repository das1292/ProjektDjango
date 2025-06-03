from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("<h3>Strona główna – API</h3><ul><li><a href='/graphql/'>GraphQL</a></li><li><a href='/api/token/'>Token (JWT)</a></li></ul>")),
    path('admin/', admin.site.urls),

    path('api/', include('kursy.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
