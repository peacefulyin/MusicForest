from django.conf.urls import url
from piano import views
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$',RedirectView.as_view(url='/home')),
    url(r'^home',views.index),
    url(r'^album/(.*)', views.list),
    url(r'^musicSheet/(.*)', views.show_sheet),
    url(r'^category/(.*)', views.category),
    url(r'^login/signin', views.signin),
    url(r'login/signup', views.signup),
    url(r'login/quit', views.quitlogin),
    url(r'findpass/(.*)', views.findpass),

]

handler404 = views.handler404