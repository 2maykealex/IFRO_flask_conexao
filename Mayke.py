from flask import Flask, render_template, request

app = Flask(__name__)

Lista = [1,2,3]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Lista.append(request.form['texto'])
    return render_template('index.html', items=Lista)


if __name__ == '__main__':
    app.run()
