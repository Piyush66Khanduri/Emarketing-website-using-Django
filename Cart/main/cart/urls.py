from django.urls import path
from cart import views

urlpatterns=[
    path(" ",views.index,name='index'),
    path("seller/",views.seller,name='seller'),
    path("veri",views.verify,name='nm'),
    path("media/",views.med),
    path("buy/",views.buyer,name="buyer"),
    path('bvr/',views.bver),
    path("customer/",views.cust,name="client"),
    path('mark/',views.market),
    #path("<int:id>",views.tree),
]