from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')  # TEST2

# Génère une clé et un objet Fernet
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Chiffrement
    return f"Valeur encryptée : {token.decode()}"  # Retourne la chaîne chiffrée

# ✅ Nouvelle route pour le décryptage
@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        # Conversion str -> bytes
        token_bytes = token.encode()
        # Déchiffrement
        valeur_dechiffree = f.decrypt(token_bytes)
        return f"Valeur déchiffrée : {valeur_dechiffree.decode()}"
    except Exception as e:
        return f"Erreur de décryptage : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
