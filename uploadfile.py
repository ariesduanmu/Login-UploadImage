import os
from flask import (Flask, Request, flash, request, redirect, 
                   url_for, send_from_directory, current_app)
from werkzeug.utils import secure_filename
from werkzeug import SharedDataMiddleware

UPLOAD_FOLDER = '/tmp'
ALLOW_EXTENSIONS = set(['txt', 'pdf', 'jpg', 'jpeg', 'gif', 'log'])

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16*1024*1024


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField('Sign In')


def allowed_file(filename):
    return "." in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOW_EXTENSIONS

@app.route('/', methods=['GET'])
def upload_file():
    return '''
<!doctype html>
<title>Upload new File</title>
<h1>Upload new File</h1>
<form action="/upload" method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    current_app.logger.debug(request.url)
    if 'file' not in request.files:
        flash("No file part")
        return redirect(request.url)
    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], 
                               filename)

app.add_url_rule('/uploads/<filename>','uploaded_file',build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app,{
    '/uploads' : app.config['UPLOAD_FOLDER']
    })
if __name__ == "__main__":
    app.run(debug=True)