from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('details/<int:vlog_id>',views.detail,name="detail"),
    path('add/',views.add,name='add'),
    path('update/<int:vlog_id>', views.update, name='update'),
    path('delete/<int:vlog_id>', views.delete, name='delete'),
    ]
