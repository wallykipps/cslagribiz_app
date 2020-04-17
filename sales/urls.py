from django.urls import path
from . import views


urlpatterns = [
    path('',views.sales, name='sales'),
    path('salesform/',views.salesform, name='salesform'),
    path('postsale/',views.postsale, name='postsale'),

]
