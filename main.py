from flask import Flask, render_template
import os # Importante para o Render

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/surpresa')
def surpresa():
    # Data de início: 15 de Setembro de 2024
    data_inicio = "2024-09-15T00:00:00"
    return render_template('surpresa.html', data_inicio=data_inicio)

if __name__ == '__main__':
    # Esta linha permite que o Render escolha a porta correta
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
