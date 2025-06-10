from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('delete_project/<int:pk>/', views.DeleteProjectView.as_view(), name='delete_project'),
    path('edit_project/<int:pk>/', views.EditProjectView.as_view(), name='edit_project'),
    path('add_project', views.AddProjectView.as_view(), name='add_project'),
    path('projects/<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('', views.IndexView.as_view(), name='home'),
]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
