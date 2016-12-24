from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
data = []
@app.route('/')
def hello_world():
    return 'Hello, cs!'


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/iras_check', methods=["POST"])
def check():
    name = request.form.get('cand')
    skl = request.form.get('skl')
    data.append(name)
    data.append(skl)
    return redirect(url_for('list'))

@app.route('/list')
def list():
    return render_template('list.html', info = data)


if __name__ == "__main__":
    app.run(debug = True)