from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /wine/
    url(r'^car$', views.car_list, name='car_list'),
    # ex: /wine/5/
    url(r'^car/(?P<car_id>[0-9]+)/$', views.car_detail, name='car_detail'),
]
