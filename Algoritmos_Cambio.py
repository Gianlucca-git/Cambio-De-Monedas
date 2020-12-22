from abc import abstractproperty
import math

def Voraz (cambio,lista_monedas):

    monedas_a_retornar=[]
    suma=0
    
    i=0
    while i <= len(lista_monedas):     

        #print("\n   valor i en lista de monedas ->",lista_monedas[i] )

        #print("\n   Cambio pendiente ->", cambio)

        resto = (cambio%lista_monedas[i]) ## el modulo del cambio en la moneda
        veces_que_esta = math.floor(cambio/lista_monedas[i]) ## saber cuantas veces esta la moneda en el cambio

        #print("\n   resto ->",resto ) 
        #print("\n   veces_que_esta ->", veces_que_esta )  

        if ( resto == 0):

            while veces_que_esta > 0:
                #print("\n   diferencia while ->", veces_que_esta ) 
                monedas_a_retornar.append(lista_monedas[i])
                veces_que_esta -=1

            return monedas_a_retornar
            
        elif (lista_monedas[i] > cambio ): ## si la moneda actual es mayor que el cambio, sigamos 
            i+=1      
        else: ## si falta completar mas para el cambio ...
            
            while veces_que_esta > 0:
                monedas_a_retornar.append(lista_monedas[i]) ## concatene la moneda actual a las monedas por retornar
                veces_que_esta -=1

            cambio= resto
            i += 1

def modificacion(cambio,monedas_totales):
 
    suma = 0
    copia_cambio = cambio
    respuesta = []
    i=0

    while i<len(monedas_totales):

       valor = monedas_totales[i][0]## representa el valor de la moneda en monedas guardadas

       cantidad_de_veces=monedas_totales[i][1] ## representa la cantidad de veces que aparece la moneda en monedas guardadas

       while (cantidad_de_veces>0):

           if (valor<=cambio):

                cambio = cambio - valor
                respuesta.append(valor)                

           else : break

           cantidad_de_veces-=1
       i+=1

    iii=0
    
    while iii<len(respuesta):
        suma = suma + respuesta[iii]
        iii+=1
    ##print ("suma", suma)
    if suma == copia_cambio :
        return respuesta
    else:
        return 0


def Dinamico (cambio,lista_monedas):

   monedas_totales =[]
   resto=0
   i=0

   while (i < len(lista_monedas)):

        resto = (cambio%lista_monedas[i]) ## el modulo del cambio en la moneda
        veces_que_esta = math.floor(cambio/lista_monedas[i]) ## saber cuantas veces esta la moneda en el cambio

        if (lista_monedas[i] < cambio ): ## si la moneda es mayor que el cambio, no la añadimos

           ##print("\n    moneda ->", lista_monedas[i])
           ##print("\n    Veces que esta ->", veces_que_esta)

           monedas_totales.append([lista_monedas[i],veces_que_esta]) ## guardamos cuantas veces esta una moneda y su valor
                                 
        i+=1

   #print("\n    Monedas Guardadas ->", monedas_totales)
   # 
   ## ahora recorremos las monedas guardadas para saber como entregar la respuesta
   # 
   
   contador_de_veces=0
   todas_las_respuestas=[]
   lista_auxiliar=[]
   i=0
   while i<len(monedas_totales):

        cantidad_de_moneda = monedas_totales[i][1]

        while cantidad_de_moneda > 0:                    

            todas_las_respuestas.append( modificacion(cambio,monedas_totales) )            
            
            cantidad_de_moneda-=1    
            monedas_totales[i][1] = cantidad_de_moneda      

        i+=1 
        
   ##print ( modificacion(cambio,[[10, 1], [6,0], [5, 0], [1,12]] ) )   
   return todas_las_respuestas





  ## funcion auxiliar para Backtracking     
def suma_guarde(guarde,lista_monedas):

    total =0
    i=0
    while i < len(lista_monedas):

        total= total + (lista_monedas[i]*guarde[i])
        i+=1

    return total 

def Backtracking (cambio,lista_monedas):

    #guardadas=[]
    guarde=[0]*len(lista_monedas)
    #check_point = 0
    
    apuntador_i=0

    while(cambio >= 0):

        #print("\n Cambio ->", cambio)

        if (apuntador_i==len(lista_monedas)): ## cuando apuntador llegue al final, se devuelve  
            #print("\n Backtracking ")
            apuntador_i = 0 

        if (suma_guarde(guarde,lista_monedas) >= cambio ): ## momento de salida, cuando la suma es mayor o igual a cambio
            #print("\n Encontre el resultado, Me salgo  ")
            
            break 

        elif ( (suma_guarde(guarde,lista_monedas)+ lista_monedas[apuntador_i]) > cambio ):
            #print("\n CONTINUO ", apuntador_i)
            apuntador_i+=1
        else:
            aux = guarde[apuntador_i] + 1 
            guarde[apuntador_i] = aux 
            #print("\n       Guardados ->>> ",guarde)
            apuntador_i+=1
    i=0
    print("\n       Guardados ->>> ",guarde)
    respuesta=[]

    while i < len(guarde) : ## bucle para dar la respuesta en monedas

        numero = guarde[i]

        while numero > 0 :

            respuesta.append(lista_monedas[i])
            numero-=1
        i+=1

    return respuesta  



def Menu():

    lista_monedas=[5,4,3,2,1] 
    cambio=7

    lista_monedas.sort(reverse = True) ## ordenamos la lista de mayor a menor para facilitar el proceso 

    if (lista_monedas.count(1)==0): # condicion para garantizar que exista una moneda con valor de 1 en lista_monedas
        print("\n\nAtencion, se agrego moneda de valor uno al sistema\n")
        lista_monedas.append(1)    

    #print ("\nPor favor elija el metodo a utilizar \n")

    ##print ("    El sistema de cambio tiene estas monedas ->",lista_monedas,"\n")

    

    ##print ("Respuesta Voraz:",Voraz(cambio,lista_monedas))

    print ("Respuesta Dinamica:",Dinamico(cambio,lista_monedas))

    ##print ("Respuesta Backtracking:",Backtracking(cambio,lista_monedas),"\n\n")
        
print("\n\n ALGORITMOS DE CAMBIO \n")
Menu()

## print(suma_guarde([1,0,3,1],[5,10,3,15])) ## funciona bien