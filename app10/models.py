# en tu aplicacion/models.py
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateField()
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta de {self.cliente.nombre} - {self.fecha_venta}"
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class TipoCliente(models.Model):
    tipocliente_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        
        return self.descripcion 

class Promocion(models.Model):
    promocion_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipomonto = models.IntegerField()
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
    
class Condiciones(models.Model):
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    def save(self, *args, **kwargs):
        self.promocion.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} en {self.promocion}'
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} en {self.venta}'
