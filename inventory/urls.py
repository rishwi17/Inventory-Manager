from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^furniture$', display_furniture, name='display_furniture'),
    url(r'^fashion$', display_fashion, name='display_fashion'),
    url(r'^gadgets$', display_gadgets, name='display_gadgets'),

    url(r'^add_furniture$', add_furniture, name="add_furniture"),
    url(r'^add_fashion$', add_fashion, name="add_fashion"),
    url(r'^add_gadgets$', add_gadgets, name="add_gadgets"),

    url(r'^furniture/edit_item/(?P<pk>\d+)$', edit_furniture, name="edit_furniture"),
    url(r'^fashion/edit_item/(?P<pk>\d+)$', edit_fashion, name="edit_fashion"),
    url(r'^gadgets/edit_item/(?P<pk>\d+)$', edit_gadgets, name="edit_gadgets"),


    url(r'^furniture/delete/(?P<pk>\d+)$', delete_furniture, name="delete_furniture"),
    url(r'^fashion/delete/(?P<pk>\d+)$', delete_fashion, name="delete_fashion"),
    url(r'^gadgets/delete/(?P<pk>\d+)$', delete_gadgets, name="delete_gadgets")


]