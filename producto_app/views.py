from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.

def inicio_vista (request):
    losproductos=Producto.objects.all()
    return render(request,"gestionarProducto.html",{"losproductos":losproductos})

def registrarProducto(request):
    if request.method == "POST":
        idproducto = request.POST.get("txtidproducto")
        nombre = request.POST.get("txtnombre")
        idsucursal = request.POST.get("txtidsucursal")
        categoria = request.POST.get("txtcategoria")
        idproveedor = request.POST.get("txtidproveedor")
        total = request.POST.get("numtotal")
        stock = request.POST.get("numstock")

        # Validar campos obligatorios
        if not idproducto or not nombre:
            return redirect("/gestionarProducto/")  # O muestra un mensaje de error, como render a una plantilla

        # Guardar el producto
        Producto.objects.create(
            idproducto=idproducto,
            nombre=nombre,
            idsucursal=idsucursal,
            categoria=categoria,
            idproveedor=idproveedor,
            total=total,
            stock=stock
        )
        return redirect("/gestionarProducto/")  # Redirige tras el guardado exitoso

def seleccionarProducto(request, idproducto):
    try:
        producto = Producto.objects.get(idproducto=idproducto)
        return render(request, "editarProducto.html", {"misproductos": producto})
    except Producto.DoesNotExist:
        # Manejo del caso en que el producto no existe
        return render(request, "error.html", {"error": "El producto no existe"})


def borrarProducto(request, idproducto):
    try:
        producto = Producto.objects.get(idproducto=idproducto)
        producto.delete()
        return redirect("/gestionarProducto/")
    except producto.DoesNotExist:
        # Manejar el caso en el que el producto no existe
        return render(request, "error.html", {"error": "El producto no existe"})


def editarProducto(request):
    if request.method == "POST":
        # Asegúrate de usar `get()` o `[]` correctamente
        idproducto = request.POST.get("txtidproducto")
        nombre = request.POST.get("txtnombre")
        idsucursal = request.POST.get("txtidsucursal")
        categoria = request.POST.get("txtcategoria")
        idproveedor = request.POST.get("txtidproveedor")
        total = request.POST.get("numtotal")
        stock = request.POST.get("numstock")

        try:
            producto = Producto.objects.get(idproducto=idproducto)
            producto.nombre = nombre
            producto.idsucursal = idsucursal
            producto.categoria = categoria
            producto.idproveedor = idproveedor
            producto.total = total
            producto.stock = stock

            producto.save()
            return redirect("/gestionarProducto/")
        except Producto.DoesNotExist:
            # Manejo del caso en que no existe el producto
            return render(request, "error.html", {"error": "El producto no existe"})

    return redirect("/gestionarProducto/")

def editarProducto(request):
    if request.method == "POST":
        idproducto = request.POST["txtidproducto"]
        nombre = request.POST["txtnombre"]
        idsucursal = request.POST["txtidsucursal"]
        categoria = request.POST["txtcategoria"]
        idproveedor = request.POST["txtidproveedor"]
        total = request.POST["numtotal"]
        stock = request.POST["numstock"]

    try:
        producto=Producto.objects.get(idproducto=idproducto)
        producto.nombre=nombre
        producto.idsucursal=idsucursal
        producto.categoria=categoria
        producto.idproveedor=idproveedor
        producto.total=total
        producto.stock=stock
        producto.save()
        return redirect("/gestionarProducto/")
    except Producto.DoesNotExist:
        # Manejo del caso en que no existe el producto
        return render(request, "error.html", {"error": "El producto no existe"})

def gestionarProducto(request):
    return render(request, 'gestionarProducto.html')