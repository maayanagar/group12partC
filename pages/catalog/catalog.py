from flask import Blueprint, render_template


catalog = Blueprint('catalog', __name__, static_folder='static', static_url_path='/catalog', template_folder='templates')


@catalog.route('/catalog')
def index():
    return render_template('catalog.html')
    #return 'hi catalog'

# @catalog.route('/', defaults={ 'page': 'index' })
# @catalog.route('/<page>')
# def show(page):
#     try:
#         return render_template('catalog.html')
#     except TemplateNotFound:
#         abort(404)
