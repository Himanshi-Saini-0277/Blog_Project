from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # path('', views.home, name="blogapp-home"),
    path('about/', views.about, name="blogapp-about"),
    path('features/', views.features_view, name='blogapp-features'),
    path('faq/', views.FAQs, name='blogapp-faq'),

    path('', PostListView.as_view(), name="blogapp-home"),
    path('post-new/', PostCreateView.as_view(), name="blogapp-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blogapp-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="blogapp-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="blogapp-delete")
]