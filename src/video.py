import os
import api
import subprocess

def main():
    def getLength(input_video):
        result = subprocess.Popen('ffprobe -i ' + input_video + ' -show_entries format=duration -v quiet -of csv="p=0"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = result.communicate()
        if output[0][:-9] == '':
            return 0
        return int(output[0][:-9])

    y = 1

    for a in range(1,7):
        dev = '{}{}'.format("dev", a)
        root = api.path + '{}/thinkalouds/'.format(dev)
        dirlist = [item for item in os.listdir(root) if os.path.isfile(os.path.join(root, item))]
        for i in dirlist:
            if i.endswith('.avi'):
                date = i[16:26].replace("_", "-")
                data_video = {
                    "description": "Video by {} from think-aloud on {}".format(dev, date),
                    "duration": getLength(root + i),
                    "id": "",
                    "interview": None,
                    "status": "PRIVATE",
                    "tag": i,
                    "thinkaloud": api.get('think-alouds', y),
                    "uri": "http://opendata.soccerlab.polymtl.ca/videos/" + i,
                    "author": "",
                    "license": ""
                }
                api.request("Video", 'videos', data_video)
                y = y + 1