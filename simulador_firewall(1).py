# PRACTICA 21
# SIMULADOR DE FILTRADO DE RED CON FIREWALL

# Lista de direcciones IP bloqueadas
lista_negra = [
    "192.168.1.100",
    "10.0.0.25",
    "172.16.0.50"
]

def verificar_ip(ip):
    print("\nAnalizando paquete...")
    print("Direccion IP de origen:", ip)

    if ip in lista_negra:
        print("ACCESO DENEGADO")
        print("La direccion IP esta bloqueada.")
    else:
        print("ACCESO PERMITIDO")
        print("La direccion IP puede acceder al servidor.")

print("================================")
print("     SIMULADOR DE FIREWALL")
print("================================")

while True:
    ip_usuario = input(
        "\nIngresa una direccion IP (o escribe salir): "
    )

    if ip_usuario.lower() == "salir":
        print("Simulacion finalizada.")
        break

    verificar_ip(ip_usuario)
