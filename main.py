############ UTILS ###############
def mostrar_menu(opciones_menu):
    print('')
    print('========== MENÚ PRINCIPAL ==========')
    for indice, op_menu in enumerate(opciones_menu):
        print(f'{indice+1}. {op_menu}')
    print('====================================')

def validar_texto(txt):
    if txt is None or txt.strip() == "":
        return False
    else:
        return True
    
def validar_entero_positivo(num):
    if num is None or num <= 0:
        return False
    else:
        return True
    
def validar_entero_mayor_cero(num):
    if num is None or num < 0:
        return False
    else:
        return True
    
def validar_opcion(op):
    if not op:
        return False
    return op.strip().upper() == "S"

def validar_opcion_unisex(op):
    if not op:
        return None
    elif op.strip().upper() ==  "S":
        return True
    elif op.strip().upper() == "N":
        return False
    
def buscar_codigo(codigo, diccionario):
    if not codigo:
        return False
    else:
        for cdg in diccionario:
            if cdg.upper() == codigo:
                return True
        return False
    
############ FIN UTILS ###############

############ CONTROLLERS ###############

def unidades_categoria(categoria ,d_prendas, dicc_bodega):
   try:
        if not d_prendas or not dicc_bodega or len(d_prendas) == 0 :
            print('No hay registros en nuestro sistema. Volverá al menú principal.')
            return
        while True:
            categoria = input('Favor ingrese categoría a validar: ').lower()
            cantidad_unidades = 0
            
            if not validar_texto(categoria):
                print('Ha ocurrido un error al ingresar la categoría. Favor intente de nuevo.')
            else:
                for elemento in d_prendas:
                    if categoria == d_prendas[elemento][1].lower():
                        cantidad_unidades += dicc_bodega[elemento][1]
                    
                print(f'Cantidad de unidades por categoria: {cantidad_unidades}')
                return
   except ValueError as error:
       print(f'Ha ocurrido un error. Error: {error}')


def eliminar_prenda(codigo, d_prendas, d_bodega):    
    d_prendas.pop(codigo)
    d_bodega.pop(codigo)
    
    return True

def busqueda_precio(p_min, p_max, d_prendas, d_bodega):
    try:
        if not d_prendas or not d_bodega or len(d_prendas) == 0 :
            print('No hay registros en nuestro sistema. Volverá al menú principal.')
            return
        
        print('Para buscar una prendas por rango de precios favor ingrese: ')

        while True:
            p_min = int(input('Precio mínimo: '))
            
            if not validar_entero_mayor_cero(p_min):
                print('Erro al ingresar el rango mínimo de precio. Favor intente de nuevo')
            else:
                break
            
                    
        while True:
            p_max = int(input('Precio máximo: '))
            
            if not validar_entero_mayor_cero(p_max):
                print('Erro al ingresar el rango máximo de precio. Favor intente de nuevo')
            else:
                break
            
        for codigo in d_bodega:
            if d_bodega[codigo][0] >= p_min and d_bodega[codigo][0] <= p_max:
                print(f'Prenda: {d_prendas[codigo][0]}')
        return
        
    except ValueError as error:
        print(f'Ha ocurrido un error en el sistema. Error: {error}')


def actualizar_precio(codigo, nuevo_precio, d_bodega):
    d_bodega[codigo][0] = nuevo_precio                
    return True

def agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades, d_prendas, d_bodega):        
    if categoria or nombre or categoria or talla or color or es_unisex or precio or unidades:
        d_prendas[codigo] = [nombre, categoria, talla, color, material, es_unisex]
        d_bodega[codigo] = [precio, unidades]
        
        return True
    

############ FIN CONTROLLERS ###############

def main():
    def leer_opcion():
        try:
            opMenu = int(input('Favor elija una de las opciones para continuar: '))
            if 1 <= opMenu <= 6:
                return opMenu
            else:
                print('Error al ingresar opción. No coincide con nuestros registros')
        except ValueError as error:
            print(f'Error al ingresar opción. Error: {error}')

    try:
        prendas = {
            'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon',
            True],
            'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
            'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester',
            True],
            'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
            'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon',
            True],
            'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon',
            False],
        }
        bodega = {
                'S001': [7990, 12],
                'S002': [19990, 0],
                'S003': [29990, 3],
                'S004': [24990, 6],
                'S005': [17990, 8],
                'S006': [14990, 2],
        }
        menu = ['Unidades por categoría', 'Búsqueda de prendas por rango de precio', 'Actualizar precio de prenda', 'Agregar prenda', 'Eliminar prenda', 'Salir']
        
        opMenu = 0

        while opMenu != 6:
            mostrar_menu(menu)      
            
            opMenu = leer_opcion()      
            
            match opMenu:
                case 1:
                    categoria = ""
                    unidades_categoria(categoria, prendas, bodega)  
                case 2:
                    p_min = 0
                    p_max = 0

                    busqueda_precio(p_min, p_max, prendas, bodega)
                case 3:
                    codigo = ""
                    nuevo_precio = 0

                    if not prendas or not bodega or len(prendas) == 0 :
                        print('No hay registros en nuestro sistema. Volverá al menú principal.')
                        continue
                        
                    codigo = input('Favor ingrese código de prenda cuyo precio desea actualizar: ').upper()
                    
                    if not validar_texto(codigo):
                        print('Error al ingresar el código del prenda. Favor intente de nuevo.')
                        continue
                        
                    if not buscar_codigo(codigo, prendas):
                        print('El código ingresado no coincide con nuestros registros. Favor intente de nuevo')
                        continue
                        
                    validar_actualizacion = input(f'El nuevo_precio del prenda {prendas[codigo][0]} es de {bodega[codigo][0]}. ¿Está seguro que desea actualizar? S/N: ')
                    
                    if validar_opcion(validar_actualizacion):
                        try:
                            nuevo_precio = int(input('Favor ingrese nuevo nuevo_precio: '))
                            
                            if validar_entero_positivo(nuevo_precio):
                                actualizar_precio(codigo, nuevo_precio, bodega)
                                print('Precio actualizado correctamente.')
                            else:
                                print('El precio debe ser mayor a cero.')
                                continue
                        
                        except ValueError as error:
                            print(f'Error: {error}')  
                    else:
                        print('Usted ha elegido no actualizar el nuevo_precio.')
                            
                case 4:
                    codigo = ""
                    nombre = ""
                    categoria = ""
                    talla = "" 
                    color = ""
                    material = ""
                    es_unisex = False
                    precio = 0
                    unidades = 0
                    
                    
                    while True:
                        codigo = input('Ingrese código de producto: ').upper()

                        if not validar_texto(codigo):
                            print('Error al ingresar el código del producto. FAvor intente de nuevo.')
                        elif buscar_codigo(codigo, prendas):
                            print("El código ingresado ya existe. Favor intente d nuevo.")
                        else:
                            break


                    while True:
                        nombre = input('Ingrese nombre del prendamento: ')
                        
                        if not validar_texto(nombre):
                            print('Error al ingresar el nombre. Favor ingrese de nuevo')
                        else:
                            break
                    
                    while True:
                        categoria = input('Ingrese la categoria del prendamento: ')
                        
                        if not validar_texto(categoria):
                            print('Error al ingresar el categoria. Favor ingrese de nuevo')
                        else:
                            break
                    
                    while True:
                        material = input('Ingrese el material del prendamento: ')
                        
                        if not validar_texto(material):
                            print('Error al ingresar el material. Favor ingrese de nuevo')
                        else:
                            break
                        
                    while True:
                        talla = input('Ingrese el talla del prendamento: ')
                        
                        if not validar_texto(talla):
                            print('Error al ingresar el talla. Favor ingrese de nuevo')
                        else:
                            break
                        
                    while True:
                        color = input('Ingrese el color de la prendamento: ')
                        
                        if not validar_texto(color):
                            print('Error al ingresar el color. Favor ingrese de nuevo')
                        else:
                            break
                    
                    while True:
                        validar_es_unisex = input('Favor indique si la prenda es unisex. Ingrese "s" para si y "n" para no: ' )
                        
                        if validar_es_unisex.strip().upper() not in ("S", "N"):
                                print('Error al indicar si es unisex. Favor ingrese de nuevo')
                        else:
                            es_unisex = validar_opcion_unisex(validar_es_unisex)
                            break
                        
                    while True:
                        try:
                            precio = int(input('Favor ingrese precio del prendamento: '))
                            
                            if not validar_entero_positivo(precio):
                                print('Error al ingresar precio. Favor intente de nuevo')
                            else:
                                break
                        
                        except ValueError as error:
                            print(f'Ha ocurrido un error al ingresar el precio del prendamento. Error: {error}')
                            
                    while True:
                        try:
                            unidades =int(input('Favor cantidad de unidades disponibles del prendamento: '))
                            
                            if not  validar_entero_mayor_cero(unidades):
                                print('Error las unidades. Favor intente de nuevo')
                            else:
                                break
                        except ValueError as error:
                            print(f'Ha ocurrido un error al ingresarlas unidades de la prenda. Error: {error}')
                    
                    if agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades, prendas, bodega):
                        print('Prenda ingresada correctamente')
                case 5:
                    codigo = ""
                    
                    if not prendas or not bodega or len(prendas) == 0 :
                        print('No existen registros ene nuestro sistema. Volverá al menú principal')
                        continue
                    
                    codigo = input('Ingrese código de prenda que desea eliminar: ').upper()
                    
                    if not validar_texto(codigo):
                        print('Error al ingresar el código de la prenda. Favor intente de nuevo.')
                    elif not buscar_codigo(codigo, bodega):
                        print('El código ingresado no coincide con nuestros registros. Favor intente de nuevo.')
                    else:
                        prenda = prendas[codigo][0]
                        opcion = input(f'¿Está seguro desea eliminar el prenda {prenda} del sistema? S/N: ')
                        
                        if not validar_opcion(opcion):
                            break
                        else:
                            eliminacion = eliminar_prenda(codigo, prendas, bodega)
                            if eliminacion:
                                print('Prenda eliminada existosamente.')
                            else: 
                                print('Usted ha elegido no eliminar prenda')
                        
                case 6:
                    print('Usted ha elegido salir del sistema!')
                    return
                case _: 
                    print('La opción ingresada no coincide con nuestro sistema. Favor intente de nuevo.')
    except ValueError as error:
        print(f'Ha ocurrido un error en el sistema. Error: {error}')
main()