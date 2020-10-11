from myservice.models.user import user_coll
from bson.json_util import dumps
from bson.json_util import loads

from flask import Blueprint,jsonify,request

mypolls = Blueprint('mypolls',__name__)
@mypolls.route('/getVotedPolls',methods=['POST'])
def myVotedPolls():
    try:
        response = request.json
        response = response.get("username")
        print(response)
        cursor = user_coll.find({"username": response},{'_id': False})
        print(cursor)
        js = loads(dumps(cursor))
        print(js)
        js = js[0]["votedPolls"]
        print(js)

        if (len(js) == 0):
            return {"success": False, "message": "you voted 0 polls"}, 400
        else:
            return {"success": True, "data": js}, 200
    except Exception as e:
        return {"success":False,"message":"you did not voted any polls "+str(e)},400

@mypolls.route('/getMyPolls',methods=['POST'])
def getMyPolls():
    try:
        response = request.get_json("username")
        response = request.json
        response = response.get("username")
        cursor = user_coll.find({"username": response},{'_id': False})
        js = loads(dumps(cursor))
        print(js)
        js = js[0]["createdPolls"]
        print(js)

        if (len(js) == 0):
            return {"success": False, "message": "you posted 0 polls"}, 400
        else:
            return {"success": True, "data": js}, 200
    except Exception as e:
        return {"success":False,"message":"you did not created any polls "+str(e)},400

