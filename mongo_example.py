import pymongo


db_client = pymongo.MongoClient("mongodb://localhost:27017")
db = db_client["MethodDataInternet"]
collection = db["magnit"]

for itm in collection.find():
    print(itm)

    MONTHS = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12,
    }

    MONTHS = {
        "янв": 1,
        "фев": 2,
        "мар": 3,
        "апр": 4,
        "май": 5,
        "июн": 6,
        "июл": 7,
        "авг": 8,
        "сен": 9,
        "окт": 10,
        "ноя": 11,
        "дек": 12,
    }