inventario = [["01","Crema Lala 450gr",20,22],
              ["02","Medias Noches",15,25],
              ["03","Danup",24,12],
              ["04","Salsa Valentina",10,12],
              ["05","PEPSI Surtido de Sabores 3l",24,24],
              ["06","Nutrileche",50,16],
              ["07","Sabritas Clásicas",20,14],
              ["08","Pepsi 3L",12,26],
              ["09","Emperador Sabores",12,15],
              ["10","Modelo 355ml",24,20]]
a = 0; corte=0
while(a==0):
    print("================ABARROTES EL GYM================")
    print("Seleccione Usuario")
    print("1.Administración, 2.Acceder a punto de Venta 3.Salir")
    pick0=int(input(">> "))
    if(pick0==1):
        print("Bienvenido al Menú de Gestión")
        print("Para Generar Inventario Pulse 1")
        print("Para hacer Corte de Caja Pulse 2")
        pickA=int(input(">> "))
        if(pickA==1):
            for i in inventario: print(i)
        elif(pickA==2):
            print("Total de ventas",corte)
            corte=0
        else: print("Seleccione una opción Valida")
    elif(pick0==2):
        k=0
        cuenta=[]; monto=0; claves=[]
        while(k==0):
            print("==============PUNTO DE VENTA================")
            clave=input("CLAVE DE PRODUCTOS: ")
            if(clave=="xx"):k=1
            elif(clave=="s"):
                print("/////////////TICKET////////////////")
                for i in cuenta: print(i)
                print("Monto a Pagar: ",monto)
                corte=corte+monto
                print("///////////////////////////////////")
                for i in claves:
                    cont=0
                    for articulo in inventario:
                        if(i==articulo[0]):
                            inventario[cont][2]=inventario[cont][2]-1
                        cont=cont+1
                cuenta=[]; monto=0; claves=[]
            else:
                claves.append(clave)
                for i in inventario:
                    if(clave==i[0]): 
                        producto=i
                        monto=monto+producto[3]
                        cuenta.append([producto[1],producto[3]])
                for i in cuenta: print(i)
                print("Monto a Pagar: ",monto)
            
    elif(pick0==3):a=1        
    else:print("Seleccione una opción Valida")