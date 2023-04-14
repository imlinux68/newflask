from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/redirect')
def redire():
    return redirect(url_for('about'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/price')
def price():
    return render_template('price.html')


if __name__ == '__main__':
    app.run()