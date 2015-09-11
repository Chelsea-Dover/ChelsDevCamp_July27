from django.conf.urls import include, url
from portfolioProjrct import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'portfolioProjrct.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^about', views.about, name='about'),
    url(r'^$', views.zen, name='zen'),
    # url(r'^javapic', views.javapic, name='javapic'),
    # url(r'^javapic_jquery', views.javapic_jquery, name='javapic_jquery')
]
