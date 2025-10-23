from django.urls import path, re_path
from store import views
app_name = 'store'

urlpatterns = [
    path('', views.ProductListView.as_view(),name='list' ),
    re_path(r'^(?P<pk>[\w-]+)/$', views.ProdView.as_view(),name='prod' ),
    #path('test/<int:Product_id>', views.product_detail, name='product_detail'),


]



#path('about/', AboutView.as_view()),
