from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hola desde el Servicio 1"

if __name__ == '__main__':
    app.run(debug=True,host='192.168.56.1', port=5054)