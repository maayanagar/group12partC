from utilities.db.mongoDB import *


def AnalyzeDB():
    # print users jsons
    users_jsons = users_col.find()
    for json in users_jsons:
        print(json)
    print()

    # print members jsons
    members_jsons = members_col.find()
    for json in members_jsons:
        print(json)
    print()

    # print trainingSessions jsons
    trainingSessions_jsons = trainingSessions_col.find()
    for json in trainingSessions_jsons:
        print(json)
    print()
