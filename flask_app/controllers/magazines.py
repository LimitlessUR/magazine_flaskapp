from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.magazine import Magazine
from flask_app.models.user import User

@app.route('/new/magazine')
def new_magazine():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new.html',user=User.get_by_id(data))


@app.route('/create/magazine',methods=['POST'])
def create_magazine():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Magazine.validate_magazine(request.form):
        return redirect('/new/magazine')
    data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "user_id": session["user_id"]
    }
    Magazine.save(data)
    return redirect('/dashboard')

@app.route('/magazine/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show.html",magazine=Magazine.get_one(data),user=User.get_by_id(user_data))

