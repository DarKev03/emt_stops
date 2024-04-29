from flask import Flask, render_template, request
from emtvlcapi import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener la parada proporcionada por el usuario desde el formulario
        parada = request.form['parada']

        # Obtener los tiempos de autobús para la parada
        tiempos = emtvlcapi.get_bus_times(parada)

        # Renderizar la plantilla HTML con los tiempos de autobús
        return render_template('resultado.html', parada=parada, tiempos=tiempos)
    
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
