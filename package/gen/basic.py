import random

from ..api import db_request

letters = db_request.get_letters()
print(letters)
