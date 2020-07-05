from django.urls import path
from font import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    # 查看
    path('shouye/',views.shouye_views,name='shouye'),
    path('shouye/<int:cid>',views.shouye_views,name='shouye'),
    #修改
    path('shouye1/',views.shouye_views1,name='shouye1'),
    path('shouye1/<int:bid>',views.shouye_views1,name='shouye1'),
    path('modify/',views.modify_views.as_view(),name='modify'),
    #注册
    path('register/',views.register_views.as_view(),name='register'),
    path('register1/',views.register1_views.as_view(),name='register1'),
    #删除
    path('delete/',views.return_views,name='delete'),
    # 密码
    path('pwd/',views.pwd_views.as_view(),name='pwd'),
    path('pwd2/',views.pwd_views2.as_view(),name='pwd2'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)