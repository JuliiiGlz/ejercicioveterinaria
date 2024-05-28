from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")



@app.route('/nosotros')
def nosotros():
    return render_template("nosotros.html")


@app.route('/perro')
def perro():
    return render_template("perro.html")

@app.route('/huron')
def huron():
    return render_template("huron.html")

@app.route('/gato')
def gato():
    return render_template("gato.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Comentarios = request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agrega' )
        cursor = conn.cursor()
        cursor.execute('insert into comenta (correo,comentarios) values (%s, %s)',(aux_Correo, aux_Comentarios))
        conn.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
