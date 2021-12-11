import librosa
import librosa.display
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
fname = './DataSet/0a983cd2-0078-4698-a048-99ac01eb167a-1433917038889-1.7-f-04-hu.wav'

def generateSpectrogram(fName, fNameOut):
	samples, sample_rate = librosa.load(fName)
	fig = plt.figure(figsize=[4,4])
	ax = fig.add_subplot(111)
	ax.axes.get_xaxis().set_visible(False)
	ax.axes.get_yaxis().set_visible(False)
	ax.set_frame_on(False)
	S = librosa.feature.melspectrogram(y=samples, sr=sample_rate)
	librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
	fig.savefig(fNameOut+'.png')

from os import listdir
from os.path import isfile, join
dataSetPath = "./DataSet/";
files = [f for f in listdir(dataSetPath) if isfile(join(dataSetPath, f))]

def getTagsFromFileName(fileName): 
	return fileName[:-4].split('-')

dataProps = []
# dataProps structure=>[age, gender]
reasons = []
# reason [reson]
for file in files:
	tags = getTagsFromFileName(file)
	dataProps.append([tags[-2], tags[-3]])
	reasons.append(tags[-1])

#generating Spectrogram for each audio in DataSet
for file in files:
	print(file)
	generateSpectrogram("DataSet/"+file, "./Spectrograms/"+file[:-4])

# preprocessing Sprectrograms
spectrograms = [f for f in listdir("./Spectrograms/") if isfile(join("./Spectrograms/", f))]
for spectrogram in spectrograms:
	print("Processing "+spectrogram+" ...")
	image = Image.open("./Spectrograms/"+spectrogram)
	box = (40, 40, 248, 248)
	cropped_image = image.crop(box)
	new_image = cropped_image.resize((100, 100))
	jpgImage = Image.new("RGB", new_image.size, (255,255,255))
	jpgImage.paste(new_image,new_image)
	jpgImage.save("./ProcessedSpectrograms/"+spectrogram[:-3]+"jpg")
	print("Processing finished successful!")

pSpectrograms = [f for f in listdir("./ProcessedSpectrograms/") if isfile(join("./ProcessedSpectrograms/", f))]
import matplotlib.image as img
image = img.imread("./ProcessedSpectrograms/"+pSpectrograms[3])
plt.imshow(image), image.shape