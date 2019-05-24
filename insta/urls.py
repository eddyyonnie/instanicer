from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   url(r'^$',views.today,name='today'),
   url(r'^welcome/$',views.welcome,name = 'welcome'),
   url(r'^image/$',views.image,name ='image'),
   url(r'^profile/',views.profile,name = 'insta-Profile'),
   url(r'^edit-profile/',views.edit_profile,name = 'edit-profile'),
   url(r'^search/', views.search_results, name='search_results'),
   url(r'^search_profile/(\d+)',views.search_profile,name = 'search_profile')
]
if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)