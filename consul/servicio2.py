from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hola desde el Servicio 2"

if __name__ == '__main__':
    app.run(host='192.168.56.1', port=5055)