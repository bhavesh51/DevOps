from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/devops/')
def hello_devops():
    return 'Hello from devops!\n'

@app.route('/about/')
def about():
    return 'about us page\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Why Hello %s!\n' % username

@app.route('/perfectvips') # dynamic route
def perfectvips():
    return 'hello from perfectvips'

@app.route('/city') # dynamic route
def city():
    return 'call from city method'

@app.route('/city1') # dynamic route
def city1():
    return 'call from city1 method'

@app.route('/city2') # dynamic route
def city2():
    return 'call from city2 method'

@app.route('/state') # dynamic route
def state():
    return 'call from state method'

@app.route('/viper') # dynamic route
def viper():
    return 'no where to run no where to hide'

@app.route('/viper1') # dynamic route
def viper1():
    return 'no where to run no where to hide demo'

@app.route('/viper2') # dynamic route
def viper2():
    return 'no where to run no where to hide demo11'

@app.route('/viper3') # dynamic route
def viper3():
    return 'no where to run no where to hide viper3'

@app.route('/viper4') # dynamic route
def viper4():
    return 'no where to run no where to hide viper4'

@app.route('/apex') # dynamic route
def apex():
    return 'call from apex method'

@app.route('/ahmedabad') # dynamic route
def ahmedabad():
    return 'call from ahmedabad method'


if __name__ == '__main__':
    app.run()