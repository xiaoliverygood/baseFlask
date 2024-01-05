from flask import Blueprint

webBlue = Blueprint('web', __name__)
from . import user
