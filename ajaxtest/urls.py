from django.urls import path
from . import views

#https://qiita.com/kkkei257/items/b3292b443699ecfb148f

app_name = 'ajaxtest'
urlpatterns = [
    path(r'', views.index, name='index'),
    # 以下を追記(views.pyのwrite()関数にデータを送信できるようにする)
    path("ajax/", views.write, name="write"),
]