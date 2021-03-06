from flask import Flask
# pip install flask-restful
from flask_restful import Api
# pip install flask-sqlalchemy
from base_datos import db
# from models.estante import EstanteModel
from controllers.estante import EstanteController
from models.autor import AutorModel
from models.libro import LibroModel
from models.autorlibro import AutorLibroModel

app = Flask(__name__)
# dialect+driver://username:password@host:port/database
# es compatible con MySQL, Oracle, PostgreSQL, SQLite
#app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/libreria'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://u6vgy263x51cqqh1:bijysg2u3v9s9ayo@durvbryvdw2sjcm5.cbetxkdyhwsb.us-east-1.rds.amazonaws.com/ewt9g4onv90qac8k'
api = Api(app=app)
@app.before_first_request
def iniciador():
    # Aca se conecta al servidor
    db.init_app(app)
    # Eliminacion de los modelos, x defecto elimina todos
    # db.drop_all(app=app)
    # Creacion de los Modelos
    db.create_all(app=app)

@app.route("/")
def inicio():
    return 'El servidor funciona correctamente'

# DEFINIR MIS RUTAS
api.add_resource(EstanteController,'/estante')
if __name__ == '__main__':
    app.run(debug=True)