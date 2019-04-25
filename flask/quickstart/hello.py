from flask import Flask, url_for, request, redirect, abort
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return ('User %s' % username) + (' Args: ' + str(request.args)) 

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/<path:anything>')
def page_not_found(anything):
    # shows page not found page
    return 'Page not found %s' % anything

@app.route('/<int:anyint>')
def int_not_found(anyint):
    # shows page for int not found
    return 'Int not found %d' % anyint

@app.route('/projects/')
def projects():
    return 'The projects page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login2', methods=['GET', 'POST'])
def login2():
    if request.method == 'POST':
        pass
        # return do_the_login()
    else:
        pass
        # return show_the_login_form()

@app.route('/invalid')
def inv():
    return redirect(url_for('doneit'))

@app.route('/donenow')
def doneit():
    abort(401)
    return 'fuck u'

@app.errorhandler(401)
def access_denied(error):
    return 'Lol u got DENIED ' + str(error)

# with app.test_request_context():
   # print(url_for('index'))  
   # print(url_for('login'))
   # print(url_for('login', next='/'))
   # print(url_for('profile', username="John Doe"))
   # print(url_for('static', filename='style.css'))
