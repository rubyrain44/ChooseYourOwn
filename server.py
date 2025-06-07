from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

#////////////////////////////////////////////////////////
# INTRO ROUTES
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/start')
def start():
    return render_template("start.html")

@app.route('/initialize', methods=['POST'])
def initialize():
    session['name'] = request.form["name"].title()
    return redirect('/start2')

@app.route('/start2')
def start2():
    return render_template("start2.html")

# ////////////////////////////////////////////////
# PATH ONE CHOICES -- VACATION
@app.route('/1a')
def path1a():
    return render_template('path1-vacation/1a.html')


# ////////////////////////////////////////////////
# PATH TWO CHOICES -- BAR/BEACH/CAVE
@app.route('/2a')
def path2a():
    return render_template('path2-barcave/2a.html')


# ////////////////////////////////////////////////
# PATH THREE CHOICES -- MUSEUM/JUNGLE
@app.route('/3a')
def path3a():
    return render_template('path3-museumjungle/3a.html')




#////////////////////////////////////////////////////////

if __name__ == "__main__":
    app.run(debug=True)