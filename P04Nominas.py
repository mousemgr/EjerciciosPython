#Calculador de Nomina

def Bruto(a):
    monto = a*120
    return monto
def Neto(bruto,extra,desc):
    ext = extra*150
    neto = bruto + ext - desc
    return neto,ext
def Recibo(neto,ext,monto,desc):
    print("///////////////////////////////////")
    print("En la presente quincena usted sumo [por 96 hrs]: ")
    print("Sueldo Bruto: ",monto)
    print("Horas Extra:  ",ext)
    print("Descuento:    ", desc)
    print("Sueldo Neto:  ",neto)

Name = input("Ingrese Nombre del Colaborador: ")
hrs = int(input("Horas Reportadas: "))
hrsX = int(input("Extras Reportadas: "))
faltas = int(input("Ausencias: "))

monto = Bruto(hrs)
desc = faltas*(120*8)
[neto,ext] = Neto(monto,hrsX,desc)
Recibo(neto,ext,monto,desc)