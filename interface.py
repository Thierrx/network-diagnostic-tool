
from flask import Flask, render_template, request, jsonify
import socket
import subprocess
import platform
import re

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/diagnosticar", methods=["POST"])
def diagnosticar():

    dominio = request.json.get("dominio", "").strip()

    if not dominio:
        return jsonify({"erro": "Digite um domínio."}), 400

    # CONSULTA DNS
    try:
        ip = socket.gethostbyname(dominio)
    except socket.gaierror:
        return jsonify({"erro": "Não foi possível localizar o domínio."}), 400

    # TESTE DE CONECTIVIDADE
    sistema = platform.system()

    if sistema == "Windows":
        comando = ["ping", "-n", "4", dominio]
    else:
        comando = ["ping", "-c", "4", dominio]

    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        encoding="cp850" if sistema == "Windows" else "utf-8",
        errors="replace",
        timeout=15
    )

    # CALCULO DA LATENCIA
    tempos = re.findall(r"tempo[=<](\d+)ms", resultado.stdout)

    if tempos:
        latencias = [int(tempo) for tempo in tempos]
        media = round(sum(latencias) / len(latencias), 2)
    else:
        media = None

    return jsonify({
        "ip": ip,
        "latencia": media,
        "conectividade": "Conectado" if resultado.returncode == 0 else "Sem resposta",
        "resultado": resultado.stdout
    })


if __name__ == "__main__":
    app.run(debug=True)
