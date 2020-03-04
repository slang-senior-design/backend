from flask import Flask, jsonify, request
import db
import dbsetup

application = Flask(__name__)

#-------------------- Do not edit above --------------------
@application.route('/')
def index():
    return '-_-'

@application.route('/db/categories')
def getCategories():
    return jsonify(db.getCategories())

@application.route('/db/terms')
def getTerms():
    return jsonify(db.getAllTerms())


@application.route('/db/categories/<category>')
def getTermsByCategory(category):
    return jsonify(db.getTermsByCategory(category))


@application.route('/db/terms/<english>')
def getTerm(english):
    return jsonify(db.getTerm(english))


#-------------------- Do not edit below --------------------

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(port=4096)