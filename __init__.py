from flask import Flask
app = Flask(__name__)
app.secret_key = "AG(ASDAGIA(*&!@"
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
