from ajedrez import app
from flask import render_template


@app.route('/')
def cuadros_tablero():
    return render_template('juego1.html', col=8, fil=8)


@app.route('/<int:columna>')
def repetir_columnas(columna):
    return render_template('juego1.html', col=columna, fil=8)


@app.route('/<int:columna>/<int:fila>')
def repetir_fila(columna, fila):
    return render_template('juego1.html', col=columna, fil=fila)
