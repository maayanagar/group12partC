from flask import Blueprint, render_template
from app import app


# page_error_handlers_NOT blueprint definition
page_error_handlers = Blueprint('page_error_handlers_NOT', __name__, static_folder='static', static_url_path='/page_error_handlers_NOT', template_folder='templates')


# Error handlers
@app.errorhandler(404)
def index(error):
    return render_template('page_not_found.html', error=error), 404
