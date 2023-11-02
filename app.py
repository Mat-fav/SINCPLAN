from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalogo_plantas')
def catalogo_plantas():
    return render_template('catalogo_plantas.html')

@app.route('/catalogo_plantas/begonia')
def begonia():
    return render_template('begonia.html')

@app.route('/catalogo_plantas/cacto')
def cacto():
    return render_template('cacto.html')

@app.route('/catalogo_plantas/crisantemo')
def crisantemo():
    return render_template('crisantemo.html')

@app.route('/catalogo_plantas/hortensia')
def hortensia():
    return render_template('hortensia.html')

@app.route('/catalogo_plantas/jasmin')
def jasmin():
    return render_template('jasmin.html')

@app.route('/catalogo_plantas/lirio')
def lirio():
    return render_template('lirio.html')

@app.route('/catalogo_plantas/orquidea')
def orquidea():
    return render_template('orquidea.html')

@app.route('/catalogo_plantas/rosa')
def rosa():
    return render_template('rosa.html')

@app.route('/catalogo_plantas/suculentas')
def suculentas():
    return render_template('suculentas.html')

@app.route('/catalogo_plantas/violeta')
def violeta():
    return render_template('violeta.html')

@app.route('/catalogo_plantas/girassol')
def girassol():
    return render_template('girassol.html')

@app.route('/catalogo_plantas/samambaia')
def samambaia():
    return render_template('samambaia.html')

if __name__ == '__main__':
    app.run(debug=True)