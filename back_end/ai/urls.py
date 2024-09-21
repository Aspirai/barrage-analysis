from django.urls import path,include
from rest_framework.routers import DefaultRouter
from ai import views

router = DefaultRouter()
router.register(r'admin',views.AdminViewSet,basename='admin')
router.register(r'barrage',views.BarrageViewSet,basename='barrage')
router.register(r'room',views.RoomViewSet,basename='room')

urlpatterns = [
    path('',include(router.urls)),
    path('index/',views.index,name='index'),
    path('test/',views.test,name='test'),



    # 传入一个int型，将数据返回给detail函数
    path('<int:Barrage_id>/',views.detail,name='detail'),
    path('<int:Barrage_id>/results/',views.results,name='results'),
    path('lately/',views.barrage_inquire,name='lately'),
    path('account_management/<str:account_id>/',views.account_management,name='account_management'),
    path('barrage_delete/<int:id>/',views.barrage_delete,name='barrage_delete'),
    path('barrage_delete_all/',views.barrage_delete_all,name='barrage_delete_all'),

    path('paging/<int:page>/',views.paging,name='paging'),
    path('pagSum/',views.pagSum,name='pagSum'),
    path('room_add/<int:room_id>/',views.room_add,name='room_add'),
]