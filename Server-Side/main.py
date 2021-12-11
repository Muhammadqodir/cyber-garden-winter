import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import requests
import datetime
import json
import pyperclip
import TrainedModel
import numpy as np
from random import randrange

cred = credentials.Certificate("firebase_admin_key.json")
firebase_admin.initialize_app(cred, {
	'databaseURL': "https://mybaby-d3065-default-rtdb.firebaseio.com/",
	'storageBucket': 'gs://mybaby-d3065.appspot.com',
	})
bucket = storage.bucket('mybaby-d3065.appspot.com')

def getResFromY(Y):
	arr = [
		"bp", "bu", "ch", "dc", "hu", "ti"
	]
	index = -1
	for y in Y.tolist():
		index += 1;
		if y == 1:
			break
	return index

def download_file(fileName):
	blob = bucket.blob(fileName)
	download_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
	pyperclip.copy(download_url)
	print("Geting download URL")
	local_filename = "downloads/"+fileName
	# NOTE the stream=True parameter below
	print("Downloading")
	with requests.get(download_url, stream=True) as r:
		r.raise_for_status()
		with open(local_filename, 'wb+') as f:
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)
	print("Downloaded")
	return local_filename

def listener(event):
	print(event.data)
	try:
		action = event.data["action"]
		if action == "recognize":
			fileName = event.data["fileName"]
			local_file = download_file(fileName)
			print("File was downloaded successfully!")
			TrainedModel.contert2vaw(local_file)
			print("Converted to WAV")
			res = TrainedModel.recognize('out.wav')
			print("Predicted!")
			print(res)
			response = {
				"accurancy": res["acc"],
				"result": res["res"]
			}
			db.reference("/responses"+event.path).set(response)
	except Exception as e:
		print(e)
		print("Error")

ref = db.reference("/requests").listen(listener)
