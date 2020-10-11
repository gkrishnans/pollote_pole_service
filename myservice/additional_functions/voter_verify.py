from myservice.models.user import user_coll
from myservice.models.poll import collections
import datetime,time

def check_whether_user_already_voted(username,poll_id):
    doc = user_coll.find_one({"username":username})

    if poll_id not in doc["votedPolls"]:
        doc["votedPolls"].append(poll_id)
        user_coll.update({"username":username},{"$set":{"votedPolls":doc["votedPolls"]}})
        return 1
    else:
        return 0

"""def pollstatus(poll_id):
    if(collections.find_one({"Poll_id":poll_id})['is_timer'] == 0):
        return 1
    else:
        local = list(map(int, collections.find_one({"Poll_id": poll_id})['End_time']))
        print("local",local)
        date_time = local
        pattern = '%d.%m.%Y'
        endtime = int(time.mktime(time.strptime(date_time,pattern)))
        print(endtime)

        now = str(datetime.datetime.now().date())
        print(now)
        date_time = now
        pattern = '%d-%m-%Y'
        nowtime = int(time.mktime(time.strptime(date_time,pattern)))

        print("now",now)

        if(nowtime<endtime):
            print("hello")
            return 1
        else:
            print("bye")
            return 0
"""
"""
        local = list(map(int, collections.find_one({"Poll_id": poll_id})['End_time'].split('/')))
        print("local",local)
        endtime = datetime.datetime(local[0], local[1], local[2], 0, 0).strftime('%s')
        now = list(map(int, str(datetime.datetime.now().date()).split('/')))
        print("now",now)
        nowtime =datetime.datetime(now[0], now[1], now[2], 0, 0).strftime('%s')
"""

