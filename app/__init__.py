from flask import Flask

app = Flask(__name__, static_url_path = "", static_folder = "templates")
app.config.from_object('config')

from app import views
