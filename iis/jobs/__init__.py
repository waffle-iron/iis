from flask import Blueprint


jobs = Blueprint('jobs', __name__,
                 template_folder='./templates')  # type: Blueprint

from . import views, models # noqa: E402, F401
