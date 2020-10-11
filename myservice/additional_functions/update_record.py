from myservice.models.user import user_coll as user_coll

def update_record(name,poll_id):

    temp_record = user_coll.find_one({"username":name})
    print(temp_record)
    temp_record['createdPolls'].append(poll_id)
    user_coll.update({"username":name},{"$set":{"createdPolls":temp_record["createdPolls"]}})

    print(temp_record)

