from flask import Flask, render_template, redirect, url_for, request, session, abort, flash

from app import app

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        username = session.get('username', 'Guest')  # Default to 'Guest' if username is not set
        return render_template("index.html", username=username)
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in ['hamzayy', 'abdul'] and password == username:  # Adjust the condition to match your authentication logic
            session['logged_in'] = True
            session['username'] = username
            flash('Successful login.')
            return redirect(url_for('index'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))
