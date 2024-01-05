from . import webBlue

@webBlue.route('/login')
def login():
    return "Hello World!"