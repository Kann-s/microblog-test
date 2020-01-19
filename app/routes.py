from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sriram'}
    return '''
    <html>
        <head>
            <title>Home Page - Sri's Microblog</title>
        </head>
        <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''
