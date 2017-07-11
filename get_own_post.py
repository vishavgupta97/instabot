from constants import  BASE_URL,APP_ACCESS_TOKEN
import requests
#REQUESTS LIBRARY IS USED FOR SENDING HTTP REQUEST

import urllib    #THIS LIBRARY IS USED FOR DOWNLOADING MEDIA FROM WORLD WIDE WEB

from PIL import Image
#PIL Is PYTHON IMAGE PROCESSING LIBRARY AND IN THIS WE WILL USE MEHODS OF THIS LIBRARY

from colorama import *
init()
#MEHOD FOR GETTING OWN POST AND DOWNLOAD IT

def get_own_post() :
    requests_url=(BASE_URL)+"users/self/media/recent/?access_token=%s"%(APP_ACCESS_TOKEN)
    print "Get Request URL:%s"%(requests_url)
    own_media=requests.get(requests_url).json()
    if own_media['meta']['code']==200 :
        if len(own_media['data']) :
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print Fore.BLUE+Style.BRIGHT+"Your image has been downloaded!"
            image = "C:\Users\gupta\PycharmProjects\instabot\\" + image_name
            img = Image.open(image)
            img.show()   #SHOWING IMAGE AFTER DOWNLOADING INSTANTLY ON THE SCREEN
                        #THIS IS VERY GOOD FEATURE OF PIL LIBRARY
            return own_media['data'][0]['id']

        else :
            print Fore.RED+"!!!Post Doesn't exists!!!"
            Style.RESET_ALL
    else :
        print Fore.RED+Style.BRIGHT+"STATUS CODE OTHER THAN 200 IS FOUND!"
    return None
