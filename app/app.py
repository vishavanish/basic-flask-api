from flask import Flask, redirect, url_for,session , Response, request, render_template

app =  Flask(__name__)
app.secret_key ='secretkeysession'
@app.route("/")
def index():
    return render_template("index.html")
    return "<h1>Hello word!!!!!</h1>"

@app.route('/welcome')
def welcome():
    if 'user' in session:
    #     return f'''
    #         <h2>Welcome {session["user"]}</h2>
    #         <a href={url_for('logout')}>Logout</a>
    # '''
        return render_template("index.html")
    return redirect(url_for('/'))

    

@app.route("/login", methods=['GET', "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form['password']
        print(username, password)
        if username =='avanish' and password=="1234":
            session['user'] = username
            return redirect(url_for('welcome'))
        else:
            return Response("Invalid credential!!")
    else:
        return '''
            <h2>Login Page<h2>
            <form method ='post' >
            <label>Username</label>
            <input type='text' name='username'>
            <label>Password</label>
            <input type='password' name='password'>
            <button>submit</button>
            </form>
    '''
    
    
@app.route('/logout')
def logout():
    # if 'user' in session:
    session.pop('user', None)
    return redirect(url_for('login'))
