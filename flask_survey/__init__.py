from flask import Flask

application = app = Flask(__name__)
app.config["SECRET_KEY"] = "760bb722fb969ca1ee600a8ac52b6a7d"

# import after app to prevent circular imports
from flask_survey import routes
