#Cajero Automático
NumCuenta = "120 236 548"
Saldo = float(14000)
Contra = "1096"

r=1
while(r==1):
    print("===========BANCOTESLA===========")
    print("Bienvenid@ a nuestra Red de Cajeros")
    Numero = input("Ingrese su Número de Cuenta [9 digitos: 000 000 000] = ")
    password = input("Ingrese su PIN [4] = ")
    
    while(NumCuenta==Numero and Contra==password and r==1):
        print("=======================================")
        print("MENU DE OPCIONES")
        print("1. Realizar un retiro")
        print("2. Realizar un Deposito")
        print("3. Consulta de Saldo")
        print("4. Pagar Servicios")
        print("5. Salir")
        pick = int(input("\nIngrese la Opción Deseada: "))
        
        if (pick==1): 
            print("RETIROS============")
            ret=float(input("Cantidad a Retirar: "))
            if (ret>Saldo): print("La cantidad excede el saldo")
            else: Saldo = Saldo - ret
        elif (pick==2): 
            print("DEPOSITOS=============")
            dep=float(input("Cantidad a Depositar: "))
            Saldo = Saldo + dep
        elif (pick==3): 
            print("CONSULTAS=============")
            print("No. de Cuenta",NumCuenta)
            print("Su saldo es de: ",Saldo)
        elif (pick==4): 
            print("Pago de servicios=====")
            con=input("Concepto de Pago: ")
            monto= float(input("Monto a Pagar: "))
            Saldo = Saldo - monto
        elif (pick==5):
            q = int(input("¿Seguro que quieres Salir [1:Si,2:No]?"))
            if(q==1): r=0
        else: print("Por favor Ingrese una Opcion Valida")
    if(NumCuenta!=Numero or Contra!=password):
        print("CUENTA O CONTRASEÑA INCORRECTA")
print("Hasta Pronto")


