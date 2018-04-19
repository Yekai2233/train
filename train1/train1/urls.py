from django.conf.urls import include, url
from django.contrib import admin
from first import views as view

urlpatterns = [
    # Examples:
    # url(r'^$', 'train1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/$', view.add, name='add'),
	url(r'^add/(\d+)/(\d+)/$', view.add2, name='add2'),
	url(r'^$', view.index, name='home')
]
