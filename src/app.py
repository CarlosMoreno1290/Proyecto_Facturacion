from flask import Flask, render_template, request, redirect, url_for    
from src.models import Base, engine 
from src.models.productos import Productos 
from src.models.categorias import Categorias 
from src.models.cliente import Clientes
from src.models.vendedor import Vendedor


app = Flask(__name__)

Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html', titulo_pagina = 'Inicio')

@app.route('/crear_producto', methods=['POST','GET'])
def crear_producto():
    if request.method == 'POST':
        descripcion = request.form.get('descripcion')
        valor_unitario = request.form.get('valor_unitario')
        Unidad_Medida = request.form.get('Unidad_Medida')
        Cantidad_Stock = request.form.get('Cantidad_Stock')
        Categoria = request.form.get('Categoria')
        producto = Productos(descripcion,valor_unitario,Unidad_Medida,Cantidad_Stock,Categoria)
        Productos.crear_producto(producto)
        return redirect(url_for('ver_producto'))
    return render_template('formulario_producto.html', titulo_pagina = 'Crear Producto')

@app.route('/ver_productos')
def ver_productos():
    productos = Productos.obtener_productos()
    return render_template('tabla_productos.html', titulo_pagina = 'Ver Productos', productos=productos)

@app.route('/crear_vendedor')
def crear_vendedor():
    return render_template('formulario_vendedor.html', titulo_pagina = 'Crear vendedor')

@app.route('/ver_vendedor')
def ver_vendedor():
    return render_template('tabla_vendedor.html', titulo_pagina = 'Ver vendedor')

@app.route('/crear_cliente')
def crear_cliente():
    return render_template('formulario_cliente.html', titulo_pagina = 'Crear cliente')

@app.route('/ver_cliente')
def ver_cliente():
    return render_template('tabla_cliente.html', titulo_pagina = 'Ver cliente')