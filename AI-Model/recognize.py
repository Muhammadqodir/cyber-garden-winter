import pickle
import librosa
import librosa.display
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
from pydub import AudioSegment
import os

current_dir = os.path.abspath(os.getcwd())
print(current_dir)

with open('LM.pkl', 'rb') as f:
    clf = pickle.load(f)

def contert2vaw(fName):
    if os.path.exists("out.wav"):
        os.remove("out.wav")
    print(os.system('ffmpeg -i '+current_dir+fName+' '+current_dir+'/out.wav'))
    
def recognize(fName):
    samples, sample_rate = librosa.load(fName)
    fig = plt.figure(figsize=[4,4])
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    S = librosa.feature.melspectrogram(y=samples, sr=sample_rate)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    fig.savefig('initialSpectrogramm.png')
    image = Image.open("initialSpectrogramm.png")
    box = (40, 40, 248, 248)
    cropped_image = image.crop(box)
    new_image = cropped_image.resize((100, 100))
    jpgImage = Image.new("RGB", new_image.size, (255,255,255))
    jpgImage.paste(new_image,new_image)
    jpgImage.save("processedSpectrogramm.jpg")
    X = []
    img = Image.open("processedSpectrogramm.jpg")
    img = np.mean(img, axis=2)
    [width1,height1]=[img.shape[0],img.shape[1]]
    arr=img.reshape(width1*height1)
    X.append(arr)

    from sklearn.preprocessing import Normalizer
    norm = Normalizer().fit(X)
    normalized_X = norm.transform(X)
    print("Before:")
    print(X[0])
    print("After:")
    print(normalized_X[0])
    Y = clf.predict(X)
    print("Result: ")
    print(Y[0])
    return Y[0]