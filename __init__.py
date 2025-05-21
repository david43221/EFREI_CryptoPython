from cryptography.fernet import Fernet, InvalidToken
from flask import Flask, render_template_string, render_template, jsonify
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')  # Page d'accueil, si tu veux l'utiliser avec HTML

# 🔐 Chiffrement avec clé utilisateur
@app.route('/encrypt/<string:key>/<string:valeur>')
def encryptage(key, valeur):
    try:
        f = Fernet(key.encode())  # Clé passée par l'utilisateur
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur de chiffrement : {str(e)}"

# 🔓 Déchiffrement avec clé utilisateur
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
        return f"Erreur de décryptage : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
