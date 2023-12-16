from django.shortcuts import render, redirect
from .forms import PromocionForm,CondicionesForms, VentaForm, DetalleVentaForm
from .models import Producto, Promocion, Condiciones, Venta, DetalleVenta

def crear_promocion(request):
    if request.method == 'POST':
        form = PromocionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_condiciones')
    else:
        form = PromocionForm()

    return render(request, 'promocion.html', {'form': form})

def crear_condiciones(request):
    if request.method == 'POST':
        detalle_form = CondicionesForms(request.POST)
        if detalle_form.is_valid():
            detalle = detalle_form.save(commit=False)
            detalle.promocion = Promocion.objects.latest('promocion_id')
            detalle.save()
    else:
        detalle_form = CondicionesForms()

    productos = Producto.objects.all()
    promociones = Promocion.objects.all()
    condiciones = Condiciones.objects.all()  # Agrega esto para mostrar las condiciones en la tabla

    return render(request, 'crear_condiciones.html', {'detalle_form': detalle_form, 'productos': productos, 'promociones': promociones, 'condiciones': condiciones})

def crear_venta(request):
    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        detalle_form = DetalleVentaForm(request.POST)
        
        if venta_form.is_valid() and detalle_form.is_valid():
            venta = venta_form.save()
            detalle = detalle_form.save(commit=False)
            detalle.venta = venta
            detalle.save()
            
            return redirect('detalle_venta', venta_id=venta.id)
    else:
        venta_form = VentaForm()
        detalle_form = DetalleVentaForm()

    return render(request, 'venta.html', {'venta_form': venta_form, 'detalle_form': detalle_form})

def detalle_venta(request, venta_id):
    venta = Venta.objects.get(pk=venta_id)
    detalles = DetalleVenta.objects.filter(venta=venta)

    return render(request, 'detalle_venta.html', {'venta': venta, 'detalles': detalles})