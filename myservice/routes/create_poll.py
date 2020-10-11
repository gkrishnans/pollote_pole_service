from myservice.models.poll import collections

from myservice.additional_functions.update_record import update_record

from myservice.models.store import store

import datetime

from flask import Blueprint, request

create = Blueprint('create_polls', __name__)
@create.route('/createPoll',methods=['POST'])
def createPoll():
    try:
        poll_id = int(store.find_one({"id": 1})["counter"])
        store.update_one({"id":1},{"$set":{"counter":poll_id+1}})
        response = request.get_json()
        if(response["is_timer"]):
            m = {
                    "Category":response["Category"],
                    "sub_category":response["sub_category"],
                    "is_timer": response["is_timer"],
                    "Start_time":response["Start_time"],
                    "End_time":response["End_time"],
                    "Poll_id":poll_id,
                    "Poll_question":response["Poll_question"],
                    "Options":response["Options"],
                    "Attachment":response["Attachment"],
                    "Is_anonymous":response["Is_anonymous"],
                    "Created_date":str(datetime.datetime.now().date()),
                    "Created_by":response["Created_by"]
                }
        else:
            m = {
                    "Category":response["Category"],
                    "sub_category":response["sub_category"],
                    "is_timer": response["is_timer"],
                    "Poll_id":poll_id,
                    "Poll_question":response["Poll_question"],
                    "Options":response["Options"],
                    "Attachment":response["Attachment"],
                    "Is_anonymous":response["Is_anonymous"],
                    "Created_date":str(datetime.datetime.now().date()),
                    "Created_by":response["Created_by"]
                }

        update_record(response["Created_by"],poll_id)
        collections.insert(m)
        return {"success":True,"message":"poll creation successfull","poll_id":poll_id},200

    except Exception as e:
        print(str(e))
        return {"success":False,"message":"error creating poll"},400

#created poll
#get subcategory wise