from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'bob'} #dummy user
    return render_template('index.html',
                           title='Home',
                           user=user)