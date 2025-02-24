from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Dummy authentication logic for POC
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "admin" and password == "admin":
            flash("Login Successful", "success")
            return redirect(url_for('architecture'))
        else:
            flash("Invalid credentials", "danger")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/architecture')
def architecture():
    # Placeholder for the architecture dashboard
    return render_template('architecture.html')

@app.route('/teaming')
def teaming():
    # Placeholder for the teaming page
    return "<h1>Teaming Page Placeholder</h1>"

if __name__ == '__main__':
    app.run(debug=True)
