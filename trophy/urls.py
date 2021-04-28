from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('registration_form/',views.signup,name='signup'),
    path("login/", views.login_request, name="login_link"),
    path("logout", views.logout_request, name= "logout"),
    path('projects/<project_id>',views.projects,name='projects'),
    path('profile/<username>', views.profile, name='profile'),
    path('uploads/',views.post_site,name='post_site'),
    path('api/profiles/', views.ProfileList.as_view(),name='profile_list'),
    path('api/projects/', views.ProjectsList.as_view(),name='projects_list'),
    path('search/', views.search_results, name='search_results')
    
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
    