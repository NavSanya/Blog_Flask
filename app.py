from flask import Flask, render_template, request, redirect, session, url_for
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')
client = MongoClient(os.getenv('MONGO_URI'))
db = client.blogDB
bcrypt = Bcrypt(app)

# User Authentication (register, login, logout)
@app.route('/register', methods=['GET', 'POST'])
def register():
        if request.method == 'POST':
                existing_user = db.users.find_one({'username' : request.form['username']})
                if existing_user:
                        return "Username already exists"
                else:
                        hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
                        db.users.insert_one({
                                'username' : request.form['username'], 
                                'password' : hashed_password
                        })
                        
                        return redirect(url_for('login'))
        return render_template('register.html')
        
@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
                user = db.users.find_one({'username' : request.form['username']})
                if user and bcrypt.check_password_hash(user['password'], request.form['password']):
                        session['username'] = request.form['username']
                        return redirect(url_for('dashboard'))
                else:
                        return "Invalid username or password"
        return render_template('login.html')
        
@app.route('/logout')
def logout():
        session.pop('username', None)
        return redirect(url_for('login'))

# Index and Dashboard
@app.route('/')
def index():
        posts = db.blogs.find()
        return render_template('index.html', posts = posts)

@app.route('/dashboard')
def dashboard():
        if 'username' in session:
                posts = db.blogs.find({'author': session['username']})
                return render_template('dashboard.html', posts = posts)
        else:
                return redirect(url_for('login'))


# Blog Create, Delete, Edit, View
@app.route('/create', methods=['GET', 'POST'])
def create():
        if 'username' in session:
                if request.method == 'POST':
                        db.blogs.insert_one({
                                'title' : request.form['title'],
                                'content' : request.form['content'],
                                'author' : session['username']
                                })
                        return redirect(url_for('dashboard'))
                return render_template('create_post.html')
        else:
                return redirect(url_for('login'))
        
@app.route('/edit/<post_id>', methods = ['GET', 'POST'])
def edit(post_id):
        if 'username' in session:
                post = db.blogs.find_one({'_id': ObjectId(post_id)})
                if request.method == 'POST':
                        db.blogs.update_one({'_id': ObjectId(post_id)}, {'$set': {
                                'title' : request.form['title'],
                                'content' : request.form['content']
                                }})
                        return redirect(url_for('dashboard'))
                return render_template('edit_post.html', post = post)
        else:
                return redirect(url_for('login'))

@app.route('/delete/<post_id>')
def delete(post_id):
        if 'username' in session:
                db.posts.delete_one({'_id': ObjectId(post_id)})
                return redirect(url_for('dashboard'))
        else:
                return redirect(url_for('login'))
        
@app.route('/post/<post_id>')
def view_post(post_id):
    post = db.blogs.find_one({'_id': ObjectId(post_id)})
    return render_template('view_post.html', post=post)

        
if __name__ == '__main__':
    app.run(debug=True)
