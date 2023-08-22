from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from learning_logs import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('', include('learning_logs.urls')),

]


if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__', include(debug_toolbar.urls))
] + urlpatterns 

