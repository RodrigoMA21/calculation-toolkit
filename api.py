from flask import Flask, request, jsonify

from services.temperatura import celsius_para_fahrenheit
from services.fatorial import calcular_fatorial

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Calculation Toolkit API",
        "endpoints": [
            "/temperatura?celsius=25",
            "/fatorial?numero=5"
        ]
    })


@app.route("/temperatura")
def temperatura():
    try:
        celsius = float(request.args.get("celsius"))
        resultado = celsius_para_fahrenheit(celsius)

        return jsonify({
            "celsius": celsius,
            "fahrenheit": resultado
        })

    except (TypeError, ValueError):
        return jsonify({"erro": "Parâmetro 'celsius' inválido"}), 400


@app.route("/fatorial")
def fatorial():
    try:
        numero = int(request.args.get("numero"))

        if numero < 0:
            return jsonify({"erro": "Número deve ser não negativo"}), 400

        resultado = calcular_fatorial(numero)

        return jsonify({
            "numero": numero,
            "fatorial": resultado
        })

    except (TypeError, ValueError):
        return jsonify({"erro": "Parâmetro 'numero' inválido"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)