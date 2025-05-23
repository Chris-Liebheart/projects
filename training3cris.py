products={}
#funcion para agregar productos
def agregar_products():
    nom=input("ingresa el nombre del producto: ")
    if nom in products:
       print('!este producto ya esta en el inventario¡')
       return
    try:
        precio= float(input("precio: "))
    except ValueError:
        print('valor invalido')
        return
    cantidad= int (input("cantidad: "))  
    products[nom]= {
        "nombre":nom,
        "precio":precio,
        "cantidad": cantidad
    }
    print(f'producto en el inventario:{nom}, precio: {precio:2f},cantidad: {cantidad}')

#funcion para consultar inventario
def inventario():
    if not products:
     print("inventario vacio")
     print('\n')
     return
    print("----inventario:---")
    print('\n')
    for nom, details in products.items():
     print(f'Producto: {nom}, precio: {details["precio"]}, Cantidad: {details["cantidad"]}')

#funcion que permite al usuario actualizar el precio   
def actualizar_precio():
    print("\n-----actualizar precio-----")

    producto=input("ingresa el producto que deseas actualizar: ")
    if not products:
     print("\n el producto no se encuentra en inventario")
     return 
    nuevo_precio= float(input("ingresa precio a actualizar: "))        
    products[producto]["precio"]=nuevo_precio

#en esta funcion se le da al usuario la opcion de eliminar el producto  
def eliminar():
    if not products:
     print("este producto no existe")
     print("\n")
     return
    print("\n eliminar producto")   
    borrar=(input("cual producto desea eliminar?: "))
    del products[borrar]
    print("este producto fue eliminado:",borrar)

#funcion para calcular el total de todo el inventario   
def total_inventario():
    valor_total = sum(map(lambda item: item[1]['precio'] * int(item[1]['cantidad']), products.items()))
    print(f"El valor total del inventario es: ${valor_total}")

#funcion de menu
def menu():
 while True:
     
    print("\nMENÚ")
    print("1.agregar un producto")
    print("2.consultar inventario")
    print("3.actualizar precio")
    print("4.eliminar producto")
    print("5.total del inventario")
    print("6.salir")
    
    opcion=input("ingresa una opcion: ")
    if opcion=="1":
       agregar_products()
    elif opcion=="2":
       inventario()
    elif opcion=="3":
       actualizar_precio()
    elif opcion=="4":
       eliminar()
    elif opcion=="5":
       total_inventario()
    elif opcion=="6":
        print("salir")
        break
    else:
        print("ingresa dato valido porfavor")
        
if __name__ == "__main__": 
    menu()
       
       
        
        
       



 
     