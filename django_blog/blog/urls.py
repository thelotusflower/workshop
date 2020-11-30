from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='main-page'),
    path('section/<section>/', views.IndexView.as_view(), name='section'),
    path('section/<section>/post/<slug>', views.PostView.as_view(), name='section-post'),
    path('post/<slug>', views.PostView.as_view(), name='post'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('post/', views.PostCreateView.as_view(), name='post-create'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)