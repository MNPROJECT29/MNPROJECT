from . import views
from django.urls import path
app_name='unicardoapp'

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('unicardo/',views.unicardo,name='unicardo'),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('base/',views.base,name='base'),
    path('add/add',views.slot_add,name='add'),
    path('update/<str:name>',views.slot_update,name='update'),
    path('delete/<str:name>',views.slot_delete,name='delete')
]
