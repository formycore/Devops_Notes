from flask import Flask

app = Flask(__name__)

# adding the routes

@app.route('/')

# return html code
def index():
	return "<h1> Hello World </h1>\n <h2> samantha </h2>"

# run the application
# basic main section
if __name__ == '__main__':
	#app.run(host, port, debug) # debug is change accordingly on the webpage
	app.run(host = '127.0.0.1', port = 5000, debug = True)
