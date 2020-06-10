import spirit
import os

files = os.listdir('./code')
suffix = ['cpp', 'CPP', 'h', 'H']
fileNames = []

for item in files:
    if item.split('.')[-1] in suffix:
        fileNames.append(item)

for file in fileNames:
    print("Transforming \"" + file + "\".....")
    try:
        spirit.highlight(file)
    except IndexError:
        print("【Error】" + file)
print("Done.")
