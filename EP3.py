import datetime, csv
# Prueba 3 Alan Caro
monto=[]
Rut= []
Reclamos= []
FechaYHora= []
def calcular_dv(rut):
    rut = ''.join(filter(str.isdigit, str(rut)))
    rut_invertido = rut[::-1]
    factores = [2, 3, 4, 5, 6, 7]
    suma = 0
    for i, digito in enumerate(rut_invertido):
        suma += int(digito) * factores[i % len(factores)]
    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        return '0'
    elif dv == 10:
        return 'K'
    else:
        return str(dv)

def verificar_rut(rut):
    if '-' in rut:
        cuerpo, dv = rut.split('-')
    else:
        cuerpo, dv = rut[:-1], rut[-1]
    dv_calculado = calcular_dv(cuerpo)
    return dv_calculado.upper() == dv.upper()

def registrar_reclamo():
    # función para registrar Reclamos
    while True:
        rt = input("Ingrese su RUT (formato 12345678-9): ")
        if verificar_rut(rt):
            Rut.append(rt)
            break
        else:
            print("RUT inválido. Por favor, intente nuevamente.")
    while True:
        try:
            mnt = int(input("Ingrese el monto del reclamo: "))
            monto.append(mnt)
            break
        except ValueError:
            print("Dato inválido. Por favor, ingrese un número entero válido.")
    rcl=input("ingrese su reclamo\n")
    Reclamos.append(rcl)
    f_h = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    FechaYHora.append(f_h)
    print("\nSe agrego Reclamo\n")

def imprimir_planilla():
    # Función para imprimir la planilla de Reclamos
    if not Reclamos:
        print("No hay reclamos registrados.\n")
    else:
        try:
            with open("reclamos.csv", "w", newline='') as csvfile:
                fieldnames = ["Rut", "Fecha y Hora", "Monto", "Reclamo"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for i in range(len(Reclamos)):
                    writer.writerow({
                        "Rut": Rut[i],
                        "Fecha y Hora": FechaYHora[i],
                        "Monto": monto[i],
                        "Reclamo": Reclamos[i]
                    })
        except IOError as e:
            print(f"Error al escribir el archivo CSV: {e}")
        print("Planilla de reclamos creada.\n")       
def mostrar_planilla():
    try:
        with open("reclamos.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            encabezado = next(reader)
            print("\t".join(encabezado))
            for row in reader:
                print("\t".join(row))
    except FileNotFoundError:
        print("El archivo de reclamos no existe. Primero debe crear la planilla.")
while True:
    opc=input("""
          seleccione que desea hacer
          1- Registrar reclamo
          2- Listar reclamos
          3- Respaldar reclamos
          4- Salir
          (recuerde ingresar el numero de la accion)""")
    if opc=="1":
        registrar_reclamo()
    elif opc=="2":
        mostrar_planilla()
    elif opc=="3":
        imprimir_planilla()
    elif opc=="4":
        print("Cerrando programa...\nHasta luego")
        break
    else:
        print("opcion invalida")