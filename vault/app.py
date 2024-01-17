from flask import Flask
import hvac

app = Flask(__name__)
client = hvac.Client(url='http://localhost:8200')
client.token = ''

@app.route('/secreto')
def mostrar_secreto():
    # Leer el secreto de Vault
    read_response = client.secrets.kv.read_secret_version(path='mi_secreto')
    secreto = read_response['data']['data']['mi_secreto']
    return f"El secreto es: {secreto}"

if __name__ == "__main__":
    app.run(debug=True,port=5053)
    
