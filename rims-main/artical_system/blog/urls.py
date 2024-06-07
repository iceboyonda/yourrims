from django.urls import path
from . import views
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index_view, name='index'),
    path('spares/', views.SparesView.as_view(), name='spares'),
    path('spares_add/<int:spare_id>', spares_add_to_cart, name='spare_add'),
    path('rims/', views.RimsView.as_view(), name='rims'),
    path('cart_add/<int:rims_id>/', cart_add, name='cart_add'),
    path('cart/', get_cart, name='cart'),
    path('cart_delete/<int:cart_id>/', delete_card, name='cart-delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)