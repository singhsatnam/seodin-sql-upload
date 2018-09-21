import api
import os
from mutagen.mp3 import MP3
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter

def main():
    y = 0
    contains = False
    for a in range(1,7):
        list = []
        dev = '{}{}'.format("dev", a)
        root = api.path + '/{}/interviews/'.format(dev)
        dirlist = [ item for item in os.listdir(root) if os.path.isfile(os.path.join(root, item)) ]

        for i in dirlist:
            if i.endswith('.rtf'):
                x = 0
                print root + i
                doc = PlaintextWriter.write(Rtf15Reader.read(open(root + i))).getvalue()
                first_index = doc.find("Clip Transcript") + 21
                second_index = doc.find("Clip Keywords") - 19
                interview_date = doc[first_index - 35:first_index - 25].replace("_", "-")
                clip_transcript = doc[first_index:second_index]
                list.append([interview_date, clip_transcript])

                while x < doc.count("Clip Transcript"):

                    if doc.find("Clip Transcript", second_index) > 0:
                        first_index = doc.find("Clip Transcript", second_index) + 21
                    else:
                        break
                    if doc.find("Clip Keywords", first_index) > 0:
                        second_index = doc.find("Clip Keywords", first_index) - 16
                    else:
                        break

                    interview_date = doc[first_index - 35:first_index - 25].replace("_", "-")
                    clip_transcript = doc[first_index:second_index]

                    print interview_date, clip_transcript

                    for sublist in list:
                        if sublist[0] == interview_date:
                            sublist[1] = sublist[1] + "\n------------------\n" + clip_transcript
                            contains = True
                    if not contains:
                        list.append([interview_date, clip_transcript])
                    contains = False

                    x = x + 1

        print list
        # print list[0][0], list[0][1]

        for i in dirlist:
            if i.endswith('.mp3'):

                tag = i[:10].replace("_","-")

                index = 0
                for sublist in list:
                    if tag.strip() == sublist[0].strip():
                        description = unicode(list[index][1], errors="ignore")
                        contains = True
                    index = index + 1
                if not contains:
                    description = ""
                contains = False

                data_audio = {
                    "description": description,
                    "duration": (MP3(api.path + '/{}/interviews/{}'.format(dev,i))).info.length,
                    "id": "",
                    "interview": api.get('interviews', y+1),
                    "status": "PRIVATE",
                    "tag": i,
                    "uri": "http://opendata.soccerlab.polymtl.ca/audios/" + i,
                    "author": "",
                    "license": ""
                }
                api.request("Audio", 'audios', data_audio)
                y = y + 1
