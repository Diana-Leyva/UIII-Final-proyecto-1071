from django.shortcuts import render, redirect
from .models import Sucursal

# Vista para listar todas las sucursales
def inicio_vista (request):
    sucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursal.html", {"sucursales": sucursales})

# Vista para registrar una nueva sucursal
def registrarSucursal(request):
    if request.method == "POST":
        idsucursal = request.POST.get("txtidsucursal")
        nombre = request.POST.get("txtnombre")
        correo = request.POST.get("txtcorreo")
        gerente = request.POST.get("txtgerente")
        direccion = request.POST.get("txtdireccion")
        telefono = request.POST.get("txttelefono")
        horario = request.POST.get("txthorario")

        # Validar campos obligatorios
        if not idsucursal or not nombre:
            return redirect("/gestionarSucursal/")  # O mostrar un mensaje de error

        # Crear la sucursal
        Sucursal.objects.create(
            idsucursal=idsucursal,
            nombre=nombre,
            correo=correo,
            gerente=gerente,
            direccion=direccion,
            telefono=telefono,
            horario=horario
        )
        return redirect("/gestionarSucursal/")  # Redirigir a la lista de sucursales

    return render(request, "registrarSucursal.html")  # Si no es POST, renderizar el formulario

# Vista para editar una sucursal existente
def editarSucursal(request, idsucursal):
    try:
        sucursal = Sucursal.objects.get(idsucursal=idsucursal)

        if request.method == "POST":
            sucursal.nombre = request.POST.get("txtnombre")
            sucursal.correo = request.POST.get("txtcorreo")
            sucursal.gerente = request.POST.get("txtgerente")
            sucursal.direccion = request.POST.get("txtdireccion")
            sucursal.telefono = request.POST.get("txttelefono")
            sucursal.horario = request.POST.get("txthorario")
            sucursal.save()
            return redirect("/gestionarSucursal/")  # Redirigir a la lista de sucursales

        return render(request, "editarSucursal.html", {"sucursal": sucursal})

    except Sucursal.DoesNotExist:
        return render(request, "error.html", {"error": "Sucursal no encontrada"})

# Vista para eliminar una sucursal
def borrarSucursal(request, idsucursal):
    try:
        sucursal = Sucursal.objects.get(idsucursal=idsucursal)
        sucursal.delete()
        return redirect("/gestionarSucursal/")  # Redirigir después de eliminar
    except Sucursal.DoesNotExist:
        return render(request, "error.html", {"error": "Sucursal no encontrada"})

def seleccionarSucursal(request, idsucursal):
    try:
        sucursal = Sucursal.objects.get(idsucursal=idsucursal)
        return render(request, "editarSucursal.html", {"sucursal": sucursal})
    except Sucursal.DoesNotExist:
        return render(request, "error.html", {"error": "sucursal no existe"})
    
