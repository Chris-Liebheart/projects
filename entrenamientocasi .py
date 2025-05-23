#estructura de funcion de descuento
def calcular_precio_descuento(compra, descuento):
        precio_descuento=compra - (compra*descuento/100)  
        return precio_descuento
    
 
    
#entrada de datos
nombre=str(input("ingrese el nombre del producto"))

#ciclo de validacion de precio unitario
preciounitario=float(input("ingrese el precio unitario del producto "))
if preciounitario < 0:
    print(f"el precio que digitaste es incorrecto ")
else:
    cantidad=int(input("ingrese la cantidad de productos adquiridos "))
    descuento=float(input("ingrese el descuento"))

    #suma de datos ingresados sin descuen
    compra=float(preciounitario*cantidad)

    
 #llamada a la funcion  
preciofinal = calcular_precio_descuento(compra,descuento)
print(f"el precio final es {preciofinal}")

print("bienvenido a la tienda de productos" "\n""\n")
print("en este espacio podras comprar los productos que desees""\n")
print("recuerda que puedes pedir el descuento que desees""\n")
print("califica nuestro servicio del uno al 10""\n")
calificacion=int(input("ingrese la calificacion "))
if calificacion < 5:
     print("grcias lamentamos que no te hayas sentido 100% comodo intentaremos mejorar""\n")
elif calificacion > 5:
     print("gracias nos legra saber que te sientes comodo con nuetro servicio")




   

#salida de precio final


    


    
    







