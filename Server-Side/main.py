import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("mybaby-d3065-firebase-adminsdk-2119n-ba1b958d33.json")
firebase_admin.initialize_app(cred, {
	'databaseURL': "https://mybaby-d3065-default-rtdb.firebaseio.com/",
	'storageBucket': 'gs://mybaby-d3065.appspot.com',
	})
bucket = storage.bucket('mybaby-d3065.appspot.com')


def listener(event):
	print(event.data)
	try:
		action = event.data["action"]
		if action == "recognize":
			fileName = event.data["fileName"]
			print(fileName)
	except Exception as e:
		print(e)
		print("Error")

ref = db.reference("/requests").listen(listener)
