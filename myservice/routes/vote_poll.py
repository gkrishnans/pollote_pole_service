from myservice.models.poll import collections
from flask import Blueprint,jsonify,request
from myservice.additional_functions.voter_verify import check_whether_user_already_voted
from myservice.additional_functions.update_votes import updateVote


vote = Blueprint('vote',__name__)
@vote.route('/votePoll',methods=['POST'])
def votePoll():
    try:
        response = request.get_json()
        Poll_id = response['Poll_id']
        username = response['username']
        Option = response["Options"]
        #Is_anonymous = response["Is_anonymous"]
        decideVotedAlreadyOrNot = check_whether_user_already_voted(username,Poll_id)

        if(decideVotedAlreadyOrNot):# check voter
            if(1):#call
                updateVote(Poll_id, Option)
                return {"success":True,"message": "user voted successfully "},200
            else:
                return {"success":False,"message": "poll expired"},200
        else:
            return {"success": False, "message": "user already voted"}, 200
    except Exception as e:
        return {"success": False, "message": "error occured in voting poll"}, 400




