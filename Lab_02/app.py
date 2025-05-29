from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher 
from cipher.vigenere import VigenereCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    plain_text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return f"Text: {plain_text} <br/> Key: {key} <br/> Encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    cipher_text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)  
    return f"Text: {cipher_text} <br/> Key: {key} <br/> Decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
