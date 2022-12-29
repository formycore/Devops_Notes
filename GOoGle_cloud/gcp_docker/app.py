import os
from flask import Flask
# flask is the web frame work
app = Flask(__name__)
@app.route('/')
def hello_python():
    target = os.environ.get('TARGET', 'Hello Samantha')
    return 'Hello {}!\n'.format(target)
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))