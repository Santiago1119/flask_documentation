from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return 'Index page'

@app.route("/hello")
def hello():
    return 'Hello, World!'

@app.route("/<name>")
def hello_world(name):
    return f"Hello, {escape(name)}"
    
#peticiones HTTP en una sola ruta
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'YA INGRESASTE INFO'
    else:
        return 'APENAS QUIERES INGRESAR INFO'

# gerera un template y se retornan los parametros en render template
@app.route("/generar_template/")
@app.route("/generar_template/<name>")
def generar_template(name=None):
    return render_template('hello.html', name=name)


#Prueba las direcciones relativas con url_for
with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('static', filename='static_css/style.css'))



