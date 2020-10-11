from bson.json_util import dumps
from bson.json_util import loads

from flask import Blueprint
import flask
from myservice.models.poll import collections


polls_category = Blueprint('getwithcat',__name__)

@polls_category.route("/getPollDetails/subcategory",methods=['GET'])
def getPolls():
    try:
        subcategory = flask.request.args.get("subcategory")
        page = flask.request.args.get("page")
        cursor = collections.find({"sub_category":subcategory},{'_id': False}).skip(5*(int(page)-1)).limit(1)
        js = loads(dumps(cursor))
        print(js)
        if(len(js) == 0):
            return {"success":False,"message":"no polls found under subcategory"},200
        else:
            return {"success": True, "data": js}, 200
    except Exception as e:
        print(e)
        return {"success":False,"message":"no polls found"+str(e)},400
