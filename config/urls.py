from django.contrib import admin
from django.urls import path,include
from pybo.views import base_views

urlpatterns = [
    # /pybo/ 페이지에 해당하는 URL 매핑을 등록
    path('pybo/', include('pybo.urls')),
    # 로그인 구현
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    # 로그인 성공 시 이동할 페이지 등록
    # / 페이지에 해당하는 urlpatterns
    path('', base_views.index, name='index'),
]
