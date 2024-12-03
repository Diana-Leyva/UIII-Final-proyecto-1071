from django.shortcuts import render, redirect
from .models import Sucursal

# Vista para listar todas las sucursales
def inicio_vista (request):
    sucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursal.html", {"sucursales": sucursales})

# Vista para registrar una nueva sucursal
def registrarSucursal(request):
    if request.method == "POST":
        codigo = request.POST.get("txtcodigo")
        nombre = request.POST.get("txtnombre")
        correo = request.POST.get("txtcorreo")
        gerente = request.POST.get("txtgerente")
        direccion = request.POST.get("txtdireccion")
        telefono = request.POST.get("txttelefono")
        horario = request.POST.get("txthorario")

        # Validar campos obligatorios
        if not codigo or not nombre:
            return redirect("/gestionarSucursal/")  # O mostrar un mensaje de error

        # Crear la sucursal
        Sucursal.objects.create(
            codigo=codigo,
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
def editarSucursal(request, codigo):
    try:
        sucursal = Sucursal.objects.get(codigo=codigo)

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
def borrarSucursal(request, codigo):
    try:
        sucursal = Sucursal.objects.get(codigo=codigo)
        sucursal.delete()
        return redirect("/gestionarSucursal/")  # Redirigir después de eliminar
    except Sucursal.DoesNotExist:
        return render(request, "error.html", {"error": "Sucursal no encontrada"})

def seleccionarSucursal(request, codigo):
    try:
        sucursal = Sucursal.objects.get(codigo=codigo)
        return render(request, "editarSucursal.html", {"sucursal": sucursal})
    except Sucursal.DoesNotExist:
        return render(request, "error.html", {"error": "sucursal no existe"})
    
