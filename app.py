from flask import Flask, flash, redirect, render_template, request, session
import os
from models import User

app = Flask(__name__)

usuario = User.User('admin','Usuario Administrador','1234admin')

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['passwd'] == usuario.passwd and request.form['user'] == usuario.id:
        session['logged_in'] = True
        return render_template('/index.html')
    else:
        flash('Algo errado com o login!')
        return redirect('/')

@app.route('/logout')
def logout():
    session['logged_in'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')

def verificaSession():
    if 'logged_in' not in session or session['logged_in'] == None:
        return False
    else:
        return True

@app.route('/index')
def index():
    if verificaSession() == False:
        return redirect('/')
    return render_template('/index.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
app.run(debug=True)