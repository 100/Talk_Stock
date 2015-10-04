import private
import pymongo

def addNumber(number):
    client = pymongo.MongoClient()
	db = client.numbers
    db.insert_one({'number': number})
    client.close()

def sendTexts():
    
