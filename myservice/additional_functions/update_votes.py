from myservice.models.poll import collections as poll_coll

def updateVote(poll_id,option):
    temp = poll_coll.find_one({"Poll_id":poll_id})
    temp["Options"][option]["votes"]+=1
    poll_coll.update_one({"Poll_id":poll_id},{"$set":{"Options":temp["Options"]}})
