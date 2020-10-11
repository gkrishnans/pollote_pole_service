from pymongo import MongoClient

#myclient = MongoClient("mongodb+srv://gokul:gokul@polloteCluster.cru4v.mongodb.net/polloteCluster?retryWrites=true&w=majority")
myclient = MongoClient("mongodb+srv://gokul:gokul@pollotecluster.cru4v.mongodb.net/polloteCluster?retryWrites=true&w=majority")
mydb = myclient["pollote"]

print(mydb.list_collection_names())

