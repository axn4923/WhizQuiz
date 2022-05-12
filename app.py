from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    return render_template('about.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/about2')
def about2():
    return render_template('about2.html')


@app.route('/about3')
def about3():
    return render_template('about3.html')


@app.route('/about4')
def about4():
    return render_template('about4.html')


@app.route('/quizOverview')
def quizOverview():
    return render_template('quizOverview.html')


@app.route('/quiz1')
def quiz1():
    return render_template('quiz1.html')


@app.route('/quiz1b')
def quiz1b():
    return render_template('quiz1b.html')


@app.route('/quiz1c')
def quiz1c():
    return render_template('quiz1c.html')


@app.route('/quiz2')
def quiz2():
    return render_template('quiz2.html')


@app.route('/quiz2b')
def quiz2b():
    return render_template('quiz2b.html')


@app.route('/quiz2c')
def quiz2c():
    return render_template('quiz2c.html')


if __name__ == '__main__':
    app.run()
