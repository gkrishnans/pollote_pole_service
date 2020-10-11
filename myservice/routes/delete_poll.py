"""
from Flask.models.poll import collections

from flask import Blueprint, request

delete_poll = Blueprint('polls', __name__)
@delete_poll.route("/polls",methods=["DELETE"])
def deletePoll():
    response = request.get_json()
    myquery = {"Poll_id":response["Poll_id"]}
    collections.delete_one(myquery)
    return({"status":"post removed successfully"})


"""