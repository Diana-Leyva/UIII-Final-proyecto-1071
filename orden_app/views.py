from django.shortcuts import render, redirect
from .models import Orden

# Vista para gestionar órdenes
def inicio_vista (request):
    ordenes = Orden.objects.all()  # Traemos todas las órdenes
    return render(request, "gestionarOrden.html", {"ordenes": ordenes})

def registrarOrden(request):
    if request.method == "POST":
        codigo = request.POST.get("txtcodigo")
        cliente = request.POST.get("txtcliente")
        direccion = request.POST.get("txtdireccion")
        estado = int(request.POST.get("txtestado"))
        forden = request.POST.get("txtforden")
        total = request.POST.get("numtotal")
        metodo_pago = int(request.POST.get("nummetodopago"))

        # Guardar la nueva orden
        Orden.objects.create(
            codigo=codigo,
            cliente=cliente,
            direccion=direccion,
            estado=estado,
            forden=forden,
            total=total,
            metodo_pago=metodo_pago
        )
        return redirect("/gestionarOrden/")  # Redirige a la página de gestión de órdenes
    
    ordenes = Orden.objects.all()

    return render(request, 'gestionarOrden.html', {'ordenes': ordenes})

def seleccionarOrden(request, codigo):
    try:
        orden = Orden.objects.get(codigo=codigo)  # Cambiado a Orden
        return render(request, "editarOrden.html", {"misordenes": orden})
    except Orden.DoesNotExist:  # Cambiado a Orden
        # Si el Orden no existe, puedes redirigir al inicio sin mostrar error
        return redirect("/gestionarOrden/")

# Vista para editar una orden existente
def editarOrden(request):
    if request.method == "POST":
            codigo = request.POST.get("txtcodigo")
            cliente = request.POST.get("txtcliente")
            direccion = request.POST.get("txtdireccion")
            estado = request.POST.get("txtestado")
            forden = request.POST.get("txtforden")
            total = request.POST.get("numtotal")
            metodo_pago = request.POST.get("nummetodopago")
    
    try:
        orden = Orden.objects.get(codigo=codigo)
        orden.cliente = cliente
        orden.direccion = direccion
        orden.estado = estado
        orden.forden = forden
        orden.total = total
        orden.metodo_pago = metodo_pago
        orden.save()
        return redirect("/gestionarOrden/")
    except Orden.DoesNotExist:
        return redirect("/gestionarOrden/")  # Si no se encuentra la orden, redirige

# Vista para borrar una orden
def borrarOrden(request, codigo):
    try:
        orden = Orden.objects.get(codigo=codigo)
        orden.delete()
        return redirect("/gestionarOrden/")
    except Orden.DoesNotExist:
        return redirect("/gestionarOrden/")  # Redirige en caso de error
