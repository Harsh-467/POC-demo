from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a strong, secure key for production

@app.route('/')
def home():
    # If the user is logged in, redirect to the dashboard
    if session.get('logged_in'):
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Simple dummy authentication for POC
        if username == "admin" and password == "admin":
            session['logged_in'] = True
            flash("Login Successful", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials", "danger")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        flash("Please login first", "warning")
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/architecture')
def architecture():
    if not session.get('logged_in'):
        flash("Please login first", "warning")
        return redirect(url_for('login'))
    return render_template('architecture.html')

@app.route('/teaming')
def teaming():
    if not session.get('logged_in'):
        flash("Please login first", "warning")
        return redirect(url_for('login'))
    return render_template('teaming.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("Logged out successfully", "success")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
