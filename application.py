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

# ......not optimal
@application.route('/db/terms/<category>')
def getTerms(category):
    # category = request.args.get('category')
    # print(category)
    if(category == None):
        return jsonify(db.getAllTerms())
    else:
        return jsonify(db.getTermsByCategory(category))

@application.route('/db/terms/<english>')
def getTerm(english):
    pass


#-------------------- Do not edit below --------------------

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(port=4096)