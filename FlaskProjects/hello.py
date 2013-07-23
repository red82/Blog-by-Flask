from flask import Flask
import flask
import flask.views
import os

app = Flask(__name__)

app.secret_key = "bacon"

#@app.route('/')
#def hello_world():
#    return '!!!!!Hello World!'

#@app.route('/login', methods=['GET','POST'])
#def login():
#    if request.method == 'POST':
#        do_the_login()
#    else:
#        show_the_login_form()

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')

    def post(self):
        result = eval(flask.request.form['expression'])
        #flask.flash(result)
        return self.get()

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])

if __name__=='__main__':
    app.debug = True
    app.run()

