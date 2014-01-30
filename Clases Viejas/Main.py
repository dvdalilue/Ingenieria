#*****************************************************************************
# Clase : main.py
#
# Descripcion : Clase que implementa el main del sistema.
#           despliega opciones para que el usuario pueda utilizar
#            el sistema
#
# Autores : Vanessa Rivas . #  carnet: 10-10608
#           Gabriel Russo   #  carnet  08-11021
# Grupo :1 
# Seccion : 1
#
#*****************************************************************************
from CLEI import CLEI
import os

if __name__ == '__main__':
    os.system("clear")
  
    def Mostrar_Menu():
        """ Metodo : Mostrar_Menu
      Parametros : self 
      Descripcion; Muestra las opciones del sistema al usuario, y atrapa la respuesta del mismo
        """
        print("Menu Principal:\n1. Crear Comite \n2. Elegir Presidente \n3. Registrar Articulo\n4. Realizar Votacion\n5. Generar lista articulos admitidos y empatados.\n6. Mostrar lista de articulos\n7. Salir")
        opcion = int(raw_input("Numero de la opcion que desea realizar:"))
        os.system("clear")
        return(opcion)
    
    

    swich= True
    #se crea una conferencia
    CLEI_2014 = CLEI()
    
    while (swich):
    # se crea el menu de opciones y se atrapa la opcion del usuario
        opcion = Mostrar_Menu()
        if opcion == 1:
            Miembros_Cp = CLEI_2014.Crear_Comite()
            os.system("clear")
        elif opcion == 2:
            if CLEI_2014.Miembros_Cp != []:
                CLEI_2014.elegir_PresidenteCP()
            os.system("clear")
        elif opcion == 3:
            CLEI_2014.Crear_Articulo()
            os.system("clear")
        elif opcion == 4:
            cod_Articulo = int(raw_input('Introduzca el Codigo del Articulo al cual desea calificar: '))
            CI = int(raw_input('Introduzca su cedula de identidad: '))
            Calificacion = int(raw_input('Calificacion: '))
            os.system("clear")
            CLEI_2014.Realizar_Votacion(cod_Articulo, CI ,Calificacion)      
        elif opcion == 5:
            N = int(raw_input('Numero maximo de articulos que seran admitidos: '))
            os.system("clear")
            a=CLEI_2014.Generar_Listas(N)
        elif opcion == 6:
            os.system("clear")
            if len(CLEI_2014.Lista_Articulos) > 0:
                for i in CLEI_2014.Lista_Articulos:
                    print(i.to_String())
        elif opcion == 7:
            swich = False
        else:
            print("\nopcion invalida\n")
            
