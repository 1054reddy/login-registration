from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

registered_users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    user_id = request.form['userId']
    user_password = request.form['userPassword']

    if user_id in registered_users:
        flash("User ID already registered!", "error")
    else:
        if len(user_password) < 6:
            flash("Password must be at least 6 characters long!", "error")
        else:
            registered_users[user_id] = user_password
            flash("Registration successful!", "success")
    
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
