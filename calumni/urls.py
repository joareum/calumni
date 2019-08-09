from django.contrib import admin
from django.urls import path
from cal import views as cal
from accounts import views as accounts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cal.home, name="home"),
    path('new/', cal.new, name="new"),
    path('create/', cal.create, name="create"),
    path('read/', cal.read, name="read"),
    path('signup/', accounts.signup, name='signup'),
    path('login/', accounts.login, name='login'),
    path('logout/', accounts.logout, name='logout'),
    path('detail/<int:post_id>/',cal.detail, name='detail'),
    path('<int:post_id>/update/', cal.update, name="update"),
    path('<int:post_id>/delete/', cal.delete, name="delete"),
    path('<int:post_id>/renew/', cal.renew, name='renew'),
    path('<int:post_id>/comment/create', cal.create_c, name="comment"),
    path('board/<str:category1>/<str:category2>/',cal.board, name="board"),
    path('board/<str:category1>',cal.bigboard, name='bigboard'),
      
] 
