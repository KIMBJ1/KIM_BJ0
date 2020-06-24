from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def if_practice():
    return render_template('asdf.html')

if __name__ == '__main__':
    app.run()