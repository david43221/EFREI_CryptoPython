from cryptography.fernet import Fernet, InvalidToken
from flask import Flask, render_template_string, render_template, jsonify
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Bienvenue sur l'API de cryptage/décryptage personnalisée !"

# 🔐 Route de chiffrement
@app.route('/encrypt/<string:key>/<string:valeur>')
def encryptage(key, valeur):
    try:
        f = Fernet(key.encode())
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur : clé invalide ou format incorrect. Détail : {str(e)}"

@app.route('/decrypt/<string:key>/<string:token>')
def decryptage(key, token):
    try:
        f = Fernet(key.encode())
        token_bytes = token.encode()
        valeur_dechiffree = f.decrypt(token_bytes)
        return f"Valeur déchiffrée : {valeur_dechiffree.decode()}"
    except InvalidToken:
        return "Erreur : le token ne peut pas être déchiffré avec cette clé."
    except Exception as e:
        return f"Erreur : clé invalide ou format incorrect. Détail : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
