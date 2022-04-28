from rest_framework.routers import SimpleRouter
from .views import FileViewSet

router = SimpleRouter()
router.register(r'files', FileViewSet)

urlpatterns = []
urlpatterns += router.urls
