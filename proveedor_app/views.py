from django.shortcuts import render, redirect
from .models import Proveedor

def inicio_vista(request):
    proveedores = Proveedor.objects.all()
    return render(request, "gestionarProveedor.html", {"proveedores": proveedores})

def proveedores_view(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'gestionarProveedor.html', {'proveedores': proveedores})


def editarProveedor(request, idproveedor):
    proveedor = Proveedor.objects.get(idproveedor=idproveedor)
    if request.method == "POST":
        proveedor.nombre = request.POST["nombre"]
        proveedor.telefono = request.POST["telefono"]
        proveedor.correo = request.POST["correo"]
        proveedor.direccion = request.POST["direccion"]
        proveedor.paginaweb = request.POST["paginaweb"]
        proveedor.tipo = int(request.POST["tipo"])  # Asegurarse de que tipo es un entero
        proveedor.save()
        return redirect("/gestionarProveedor")
    return render(request, "editarProveedor.html", {"proveedor": proveedor})



def registrarProveedor(request):
    if request.method == "POST":
        # Obtener los valores del formulario
        idproveedor = request.POST.get("txtidproveedor")
        nombre = request.POST.get("txtnombre")
        telefono = request.POST.get("txttelefono")
        correo = request.POST.get("txtcorreo")
        direccion = request.POST.get("txtdireccion")
        paginaweb = request.POST.get("txtpaginaweb")
        tipo = int(request.POST.get("txttipo"))  # Convertir tipo a entero

        # Validar campos obligatorios
        if not idproveedor or not nombre:
            return redirect("/gestionarProveedor/")  # O muestra un mensaje de error

        # Guardar el proveedor
        Proveedor.objects.create(
            idproveedor=idproveedor,
            nombre=nombre,
            telefono=telefono,
            correo=correo,
            direccion=direccion,
            paginaweb=paginaweb,
            tipo=tipo
        )

        # Redirigir tras el guardado exitoso
        return redirect("/gestionarProveedor/")  # O a otra URL específica para proveedores

    # Obtener todos los proveedores para el listado
    proveedores = Proveedor.objects.all()

    return render(request, 'gestionarProveedor.html', {'proveedores': proveedores})


def seleccionarProveedor(request, idproveedor):
    try:
        proveedor = Proveedor.objects.get(idproveedor=idproveedor)
        return render(request, "editarProveedor.html", {"proveedor": proveedor})
    except Proveedor.DoesNotExist:
        return render(request, "error.html", {"error": "El proveedor no existe"})
    
def borrarProveedor(request, idproveedor):
    try:
        proveedor = Proveedor.objects.get(idproveedor=idproveedor)
        proveedor.delete()  # Eliminar el proveedor seleccionado
        return redirect("/")
    except Proveedor.DoesNotExist:
        return render(request, "error.html", {"error": "El proveedor no existe"})

