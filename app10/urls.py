from django.urls import path
from .views import crear_promocion, crear_condiciones, crear_venta, detalle_venta

urlpatterns = [
    path('crear_promocion/', crear_promocion, name='crear_promocion'),
    path('crear_condiciones/', crear_condiciones, name='crear_condiciones'),
    path('crear_venta/', crear_venta, name='crear_venta'),
    path('detalle_venta/<int:venta_id>/', detalle_venta, name='detalle_venta'),
    # otras URLs pueden ir aquí
]