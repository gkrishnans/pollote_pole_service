from bson.json_util import dumps
from bson.json_util import loads
import flask
from flask import Blueprint
from myservice.models.poll import collections

get_poll_id = Blueprint('get',__name__)

@get_poll_id.route('/getPollDetails/id',methods=['GET'])
def getPolls():
    try:
        id = flask.request.args.get("id")
        cursor = collections.find_one({"Poll_id":int(id)},{'_id': False})

        js = loads(dumps(cursor))
        print(js)
        if(len(js) == 0):
            return {"success": False, "message": "no polls found"}, 200
        else:
            return {"success": True, "data": js}, 200
    except Exception as e:
        return {"success":False,"message":"error creating poll"+str(e)},400

