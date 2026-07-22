import subprocess
from getpass import getuser

# Deteccion del usuario en sesion
user = getuser()

# Nombre del dispositivo (HOST)
host = subprocess.run("hostname", capture_output=True, text=True)
host = host.stdout

# Ip Tailscale del dispositivo
try:
    tip = subprocess.run(["tailscale", "ip"], capture_output=True, text=True)
    tip = tip.stdout
except:
    tip = "Tailscale ip is unknown"

# Dispositivos Tailcale disponibles
try:
    tdev = subprocess.run(["tailscale", "status", "--active"], capture_output=True, text=True)
    tdev = tdev.stdout
except:
    tip = "Tailscale ip is unknown"

# Generacion de cabecera del programa
def cabecera():
    print("--------------------------------------------------------")
    print("Envio De Archivos Mediante TailDrop De Tailscale")
    print("--------------------------------------------------------")

# Impresion de informacion
def sysinfo(host, tip):
    print("Informacion De tailcale")
    print("--------------------------------------------------------")
    print(f"Nombre del host actual:  {host}.")
    print(f"Ip Tailcale del host actual(IpV4/IpV6):  \n{tip}")

# Captura de dispositivos activos
def devices(list):
    print(f"Dispositivos disponibles:\n--------------------------------------------------------\n{tdev}")

# Solicitud del nombre de archivo
def file():
    archivo = input("Ingresa la ruta y nombre completo del archivo a enviar:   ")
    return archivo

def dest():
    destiny = input("Ingresa el nombre del dispositivo destino:   ")
    return destiny

def confirm(archivo, device):
    subprocess.run("clear")
    print("Confirma los datos antes de continuar:")
    print("--------------------------------------------------------")
    print(f"Archivo A Enviar:  {archivo}")
    print(f"Dispositivo Destino:  {device}")
    respuesta = input("Y/N\n")
    if (respuesta  == "Y") or (respuesta == "y") or (respuesta == "s"):
        print("Envio confirmado")
        try:
            subprocess.run(["tailscale", "file", "cp", f"{archivo}", f"{device}:"])
        except:
            print("El envio fallo")
        return "OK"
    if (respuesta  == "N") or (respuesta == "n"):
        print("Procedimiento cancelado")
        return "NO"
    else:
        print("Respuesta no recibida")
        return "REP"

###########################################################################################################################################

# Impresion mediante funciones
cabecera()
sysinfo(host, tip)
devices(tdev)
archivo = file()
device = dest()
sal = confirm(archivo, device)
if sal == "OK":
    print("\nFinalizado")
    print("PRESIONA ENTER PARA SALIR...")
    input()
    exit()
if sal == "NO":
    print("PRESIONA ENTER PARA SALIR...")
    input()
    exit()
if sal == "REP":
    subprocess.run("clear")
    sal = confirm(archivo, device)