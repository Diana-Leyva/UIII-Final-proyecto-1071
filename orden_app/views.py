from django.shortcuts import render, redirect
from .models import Orden

# Vista para gestionar órdenes
def inicio_vista (request):
    ordenes = Orden.objects.all()  # Traemos todas las órdenes
    return render(request, "gestionarOrden.html", {"ordenes": ordenes})

def registrarOrden(request):
    if request.method == "POST":
        idorden = request.POST.get("txtidorden")
        idcliente = request.POST.get("txtidcliente")
        idempleado = request.POST.get("txtidempleado")
        idsucursal = request.POST.get("txtidsucursal")
        forden = request.POST.get("txtforden")
        total = request.POST.get("numtotal")
        idproducto = request.POST.get("txtidproducto")

        # Guardar la nueva orden
        Orden.objects.create(
            idorden=idorden,
            idcliente=idcliente,
            idempleado=idempleado,
            idsucursal=idsucursal,
            forden=forden,
            total=total,
            idproducto=idproducto
        )
        return redirect("/gestionarOrden/")  # Redirige a la página de gestión de órdenes
    
    ordenes = Orden.objects.all()

    return render(request, 'gestionarOrden.html', {'ordenes': ordenes})

def seleccionarOrden(request, idorden):
    try:
        orden = Orden.objects.get(idorden=idorden)  # Cambiado a Orden
        return render(request, "editarOrden.html", {"misordenes": orden})
    except Orden.DoesNotExist:  # Cambiado a Orden
        # Si el Orden no existe, puedes redirigir al inicio sin mostrar error
        return redirect("/gestionarOrden/")

# Vista para editar una orden existente
def editarOrden(request):
    if request.method == "POST":
            idorden = request.POST.get("txtidorden")
            idcliente = request.POST.get("txtidcliente")
            idempleado = request.POST.get("txtidempleado")
            idsucursal = request.POST.get("txtidsucursal")
            forden = request.POST.get("txtforden")
            total = request.POST.get("numtotal")
            idproducto = request.POST.get("numidproducto")
    
    try:
        orden = Orden.objects.get(idorden=idorden)
        orden.idcliente = idcliente
        orden.idempleado = idempleado
        orden.idsucursal = idsucursal
        orden.forden = forden
        orden.total = total
        orden.idproducto = idproducto
        orden.save()
        return redirect("/gestionarOrden/")
    except Orden.DoesNotExist:
        return redirect("/gestionarOrden/")  # Si no se encuentra la orden, redirige

# Vista para borrar una orden
def borrarOrden(request, idorden):
    try:
        orden = Orden.objects.get(idorden=idorden)
        orden.delete()
        return redirect("/gestionarOrden/")
    except Orden.DoesNotExist:
        return redirect("/gestionarOrden/")  # Redirige en caso de error
