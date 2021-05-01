from django.urls import path
from .views import (
     homepage, major_create, major_List, major_detail, major_update, major_delete,
Ma_disListView, Ma_disDetailView, Ma_disCreateView, Ma_disDeleteView
)
app_name= "helpdesk"

urlpatterns = [
    
    path('', homepage, name='homepage'),
    path('create/', Ma_disCreateView.as_view(), name='Major-create'),
    path('Ma_list/', Ma_disListView.as_view(), name='major-list'),
    path('helpdesk/<int:pk>/', major_detail, name='major-detail'),
    path('helpdesk/<int:pk>/update', major_update, name='major-update'),
    path('helpdesk/<int:pk>/delete', Ma_disDeleteView.as_view(), name='major-delete'),

    
]
