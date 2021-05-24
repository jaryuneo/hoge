from django.urls import path
from . import views

#views(html)を呼び出す。空urlの時(つまりデフォルト画面)にtest2.htmlを表示する。
#pkはプライマリーキー。つまりファイルを一意に指定する主キー。これを送るとファイルごとに管理可能となる。
app_name='myapp'
urlpatterns=[
    path('',views.test2,name="test2"),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('histtest.png/<int:pk>/', views.histtests, name='histtest'),
]