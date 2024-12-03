from django.shortcuts import render, redirect
from .models import Empleado  # Importar el modelo Empleado

def inicio_vista(request):
    los_empleados = Empleado.objects.all()  # Recupera todos los empleados
    return render(request, "gestionarEmpleado.html", {"los_empleados": los_empleados})

def registrarEmpleado(request):
    if request.method == "POST":
        codigo = request.POST.get("txtcodigo")
        nombre = request.POST.get("txtnombre")
        telefono = request.POST.get("txttelefono")
        direccion = request.POST.get("txtdireccion")
        correo = request.POST.get("txtcorreo")
        turno = request.POST.get("numturno")
        posicion = request.POST.get("numposicion")

        # Validar campos obligatorios
        if not codigo or not nombre:
            return redirect("/gestionarEmpleado/")  # O muestra un mensaje de error, como render a una plantilla

        # Guardar el empleado
        Empleado.objects.create(
            codigo=codigo,
            nombre=nombre,
            telefono=telefono,
            direccion=direccion,
            correo=correo,
            turno=turno,
            posicion=posicion
        )
        return redirect("/gestionarEmpleado/")  # Redirige tras el guardado exitoso

    return redirect("/gestionarEmpleado/")  # Si no es POST, redirigir al inicio

def seleccionarEmpleado(request, codigo):
    try:
        empleado = Empleado.objects.get(codigo=codigo)
        return render(request, "editarEmpleado.html", {"mis_empleados": empleado})
    except Empleado.DoesNotExist:
        return redirect("/gestionarEmpleado/")

def borrarEmpleado(request, codigo):
    try:
        empleado = Empleado.objects.get(codigo=codigo)
        empleado.delete()
        return redirect("/gestionarEmpleado/")
    except Empleado.DoesNotExist:
        return redirect("/gestionarEmpleado/")

def editarEmpleado(request):
    if request.method == "POST":
        codigo = request.POST["txtcodigo"]
        nombre = request.POST["txtnombre"]
        telefono = request.POST["txttelefono"]
        direccion = request.POST["txtdireccion"]
        correo = request.POST["txtcorreo"]
        turno = request.POST["numturno"]
        posicion = request.POST["numposicion"]

        try:
            empleado = Empleado.objects.get(codigo=codigo)
            empleado.nombre = nombre
            empleado.telefono = telefono
            empleado.direccion = direccion
            empleado.correo = correo
            empleado.turno = turno
            empleado.posicion = posicion
            empleado.save()
            return redirect("/gestionarEmpleado/")
        except Empleado.DoesNotExist:
            return redirect("/gestionarEmpleado/")

    return redirect("/gestionarEmpleado/")  # Si no es POST, redirige al inicio

def gestionarEmpleado(request):
    return render(request, 'gestionarEmpleado.html')