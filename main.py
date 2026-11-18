
import socket
import subprocess
import platform
import re

print("================================")
print("     NETWORK DIAGNOSTIC TOOL")
print("================================")

dominio = input("Digite um dominio: ")

# ETAPA 1 - CONSULTA DNS
try:
    ip = socket.gethostbyname(dominio)

    print(f"\nDominio: {dominio}")
    print(f"Endereco IP: {ip}")
    print("Consulta DNS realizada com sucesso!")

except socket.gaierror:
    print("Erro: nao foi possivel encontrar o endereco IP.")

# ETAPA 2 - TESTE DE CONECTIVIDADE
print("\nTestando conectividade...")

sistema = platform.system()

if sistema == "Windows":
    comando = ["ping", "-n", "4", dominio]
else:
    comando = ["ping", "-c", "4", dominio]

resultado = subprocess.run(
    comando,
    capture_output=True,
    text=True,
    encoding="cp850",
    errors="replace"
)

# ETAPA 3 - RESULTADO E LATENCIA
if resultado.returncode == 0:
    print("\nStatus: Servidor respondeu!")
    print("\nResultado do teste:")
    print(resultado.stdout)

    tempos = re.findall(r"tempo[=<](\d+)ms", resultado.stdout)

    if tempos:
        latencias = [int(tempo) for tempo in tempos]
        media = sum(latencias) / len(latencias)

        print(f"\nLatencia media: {media:.2f} ms")

    else:
        print("\nNao foi possivel calcular a latencia.")

else:
    print("\nStatus: Servidor nao respondeu!")
