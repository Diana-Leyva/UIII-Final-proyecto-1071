from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.

def inicio_vista (request):
    losproductos=Producto.objects.all()
    return render(request,"gestionarProducto.html",{"losproductos":losproductos})

def registrarProducto(request):
    if request.method == "POST":
        codigo = request.POST.get("txtcodigo")
        nombre = request.POST.get("txtnombre")
        descripcion = request.POST.get("txtdescripcion")
        categoria = request.POST.get("txtcategoria")
        proveedor = request.POST.get("txtproveedor")
        total = request.POST.get("numtotal")
        stock = request.POST.get("numstock")

        # Validar campos obligatorios
        if not codigo or not nombre:
            return redirect("/gestionarProducto/")  # O muestra un mensaje de error, como render a una plantilla

        # Guardar el producto
        Producto.objects.create(
            codigo=codigo,
            nombre=nombre,
            descripcion=descripcion,
            categoria=categoria,
            proveedor=proveedor,
            total=total,
            stock=stock
        )
        return redirect("/gestionarProducto/")  # Redirige tras el guardado exitoso

def seleccionarProducto(request, codigo):
    try:
        producto = Producto.objects.get(codigo=codigo)
        return render(request, "editarProducto.html", {"misproductos": producto})
    except Producto.DoesNotExist:
        # Manejo del caso en que el producto no existe
        return render(request, "error.html", {"error": "El producto no existe"})


def borrarProducto(request, codigo):
    try:
        producto = Producto.objects.get(codigo=codigo)
        producto.delete()
        return redirect("/gestionarProducto/")
    except producto.DoesNotExist:
        # Manejar el caso en el que el producto no existe
        return render(request, "error.html", {"error": "El producto no existe"})


def editarProducto(request):
    if request.method == "POST":
        # Asegúrate de usar `get()` o `[]` correctamente
        codigo = request.POST.get("txtcodigo")
        nombre = request.POST.get("txtnombre")
        creditos = request.POST.get("numcredito")

        try:
            producto = Producto.objects.get(codigo=codigo)
            producto.nombre = nombre
            producto.creditos = creditos
            producto.save()
            return redirect("/gestionarProducto/")
        except Producto.DoesNotExist:
            # Manejo del caso en que no existe el producto
            return render(request, "error.html", {"error": "El producto no existe"})

    return redirect("/gestionarProducto/")

def editarProducto(request):
    if request.method == "POST":
        codigo = request.POST["txtcodigo"]
        nombre = request.POST["txtnombre"]
        descripcion = request.POST["txtdescripcion"]
        categoria = request.POST["txtcategoria"]
        proveedor = request.POST["txtproveedor"]
        total = request.POST["numtotal"]
        stock = request.POST["numstock"]

    try:
        producto=Producto.objects.get(codigo=codigo)
        producto.nombre=nombre
        producto.descripcion=descripcion
        producto.categoria=categoria
        producto.proveedor=proveedor
        producto.total=total
        producto.stock=stock
        producto.save()
        return redirect("/gestionarProducto/")
    except Producto.DoesNotExist:
        # Manejo del caso en que no existe el producto
        return render(request, "error.html", {"error": "El producto no existe"})

def gestionarProducto(request):
    return render(request, 'gestionarProducto.html')