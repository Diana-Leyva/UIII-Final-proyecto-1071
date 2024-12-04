from django.shortcuts import render, redirect
from .models import Cliente  # Cambiado a Cliente
# Create your views here.

def inicio_vista(request):
    losclientes = Cliente.objects.all()  # Cambiado a Cliente
    return render(request, "gestionarCliente.html", {"losclientes": losclientes})

def registrarCliente(request):
    if request.method == "POST":
        idcliente = request.POST.get("txtidcliente")
        nombre = request.POST.get("txtnombre")
        telefono = request.POST.get("txttelefono")
        direccion = request.POST.get("txtdireccion")
        correo = request.POST.get("txtcorreo")
        fnacimiento = request.POST.get("txtfnacimiento")
        fregistro = request.POST.get("txtfregistro")

        # Validar campos obligatorios
        if not idcliente or not nombre:
            return redirect("/gestionarCliente/")  # Redirige si hay campos obligatorios vacíos

        # Guardar el cliente
        Cliente.objects.create(
            idcliente=idcliente,
            nombre=nombre,
            telefono=telefono,
            direccion=direccion,
            correo=correo,
            fnacimiento=fnacimiento,
            fregistro=fregistro
        )
        return redirect("/gestionarCliente/")  # Redirige tras el guardado exitoso

    return redirect("/gestionarCliente/")  # Si no es POST, redirigir al inicio

def seleccionarCliente(request, idcliente):
    try:
        cliente = Cliente.objects.get(idcliente=idcliente)  # Cambiado a Cliente
        return render(request, "editarCliente.html", {"misclientes": cliente})
    except Cliente.DoesNotExist:  # Cambiado a Cliente
        # Si el cliente no existe, puedes redirigir al inicio sin mostrar error
        return redirect("/gestionarCliente/")

def borrarCliente(request, idcliente):
    try:
        cliente = Cliente.objects.get(idcliente=idcliente)  # Cambiado a Cliente
        cliente.delete()
        return redirect("/gestionarCliente/")
    except Cliente.DoesNotExist:  # Cambiado a Cliente
        # Si el cliente no existe, redirige al inicio
        return redirect("/gestionarCliente/")

def editarCliente(request):
    if request.method == "POST":
        idcliente = request.POST["txtidcliente"]
        nombre = request.POST["txtnombre"]
        telefono = request.POST["txttelefono"]
        direccion = request.POST["txtdireccion"]
        correo = request.POST["txtcorreo"]
        fnacimiento = request.POST["txtfnacimiento"]
        fregistro = request.POST["txtfregistro"]

        try:
            cliente = Cliente.objects.get(idcliente=idcliente)  # Cambiado a Cliente
            cliente.nombre = nombre
            cliente.telefono = telefono
            cliente.direccion = direccion
            cliente.correo = correo
            cliente.fnacimiento = fnacimiento
            cliente.fregistro = fregistro
            cliente.save()
            return redirect("/gestionarCliente/")
        except Cliente.DoesNotExist:  # Cambiado a Cliente
            # Si el cliente no existe, redirige al inicio
            return redirect("/gestionarCliente/")

    return redirect("/gestionarCliente/")  # Si no es POST, redirige al inicio

def gestionarCliente(request):
    return render(request, 'gestionarCliente.html')