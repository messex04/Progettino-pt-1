from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


db = SQLAlchemy(app)

class ListaSpesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    elemento = db.Column(db.String(100), nullable=False)  


with app.app_context():
    db.create_all()

@app.route('/')
def home():


    lista_spesa = ListaSpesa.query.all()
    return render_template('index.html', lista=lista_spesa)


@app.route('/aggiungi', methods=['POST'])
def aggiungi():

    elemento = request.form['elemento']
    if elemento:  
        nuovo_elemento = ListaSpesa(elemento=elemento)  
        db.session.add(nuovo_elemento) 
        db.session.commit()
    return redirect(url_for('home'))  


@app.route('/rimuovi/<int:id>', methods=['POST'])
def rimuovi(id):
  
    elemento_da_rimuovere = ListaSpesa.query.get(id)
    if elemento_da_rimuovere:  
        db.session.delete(elemento_da_rimuovere) 
        db.session.commit()  
    return redirect(url_for('home'))  


@app.route('/svuota', methods=['POST'])
def svuota_lista():
    ListaSpesa.query.delete() 
    db.session.commit()  
    return redirect(url_for('home'))  

if __name__ == '__main__':
    app.run(debug=True)  