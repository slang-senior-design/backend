from flask import Flask, jsonify
import db

application = Flask(__name__)

#-------------------- Do not edit above --------------------
@application.route('/')
def index():
    return '-_-'


@application.route('/db/<id>')
def test(id):
    return jsonify(db.selectTable())


#-------------------- Do not edit below --------------------

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(port=4096)