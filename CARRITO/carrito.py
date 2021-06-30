class Carrito:
    def __init__(self, request) :
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"]  = {}
        self.carrito = carrito
    
    def añadir (self, PRODUCTO):
        if str(PRODUCTO.id) not in self.carrito.keys():
            self.carrito[PRODUCTO.id] = {
                "PRODUCTO_id": PRODUCTO.id,
                "Nombre": PRODUCTO.nombre,
                "cantidad": 1,
                "precio": str(PRODUCTO.precio),
                "imagen": PRODUCTO.imagen.url
            }
        else:
            for key, value in self.carrito.items():
                if key == str(PRODUCTO.id):
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.save()

    def save (self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def remove(self, PRODUCTO):
        producto_id = str(PRODUCTO.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.save()

        
    def decrementar(self, PRODUCTO):
        for key, value in self.cart.items():
            if key == str(PRODUCTO.id):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 1:
                    self.remove(PRODUCTO)
                break
            else:
                print("El producto no existe en el carrito")

    def clear(self):
        self.session["carrito"] = {}
        self.session.modified = True