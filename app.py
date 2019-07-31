from flask import Flask
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('mycoolapp1.html')
    # return 'Hello, World test!'

if __name__ == '__main__':
    app.run(debug=True)

