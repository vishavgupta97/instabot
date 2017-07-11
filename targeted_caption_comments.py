import requests
from get_user_id import get_user_id
from constants import BASE_URL,APP_ACCESS_TOKEN
from get_post_id import get_post_id
insta_username="vishavgupta97"
def target_caption_comments(insta_username): #takes argument as insta username
    user_id = get_user_id(insta_username)    #url of tags has been used
    if user_id==None :
        print "Ooop!!! User Doesn't exist !!!"
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    caption_info = requests.get(request_url).json()

    if caption_info['meta']['code'] == 200:

        if len(caption_info['data']):

            for y in range(0, len(caption_info['data'])):

                caption_text = caption_info['data'][y]['caption']['text']
                caption = caption_text.split(" ")
                if 'pizza' in caption or 'PIZZA' in caption:

                    print 'Read Caption: %s' % (caption)
                    media_id = get_post_id(insta_username)
                    comment_text="Dominoz is discounting upto 50% rates in pizza this week.checkout best price for" \
                                 "you at www.vishavmarkets.com.Best prices of BADDI"
                    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
                    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
                    print 'POST request url : %s' % (request_url)

                    make_comment = requests.post(request_url, payload).json()

                    if make_comment['meta']['code'] == 200:
                        print "Successfully Posted Targetted Comment!"
                elif 'coffee' in caption or 'COFFEE' in caption:

                        print 'Read Caption: %s' % (caption)
                        media_id = get_post_id(insta_username)
                        comment_text ="Enjoy Your Coffee at suitable price with your partner at best prices..." \
                                      "vishavmarkets.com Is Waiting For Your access"
                        payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
                        request_url = (BASE_URL + 'media/%s/comments') % (media_id)
                        print 'POST request url : %s' % (request_url)

                        make_comment = requests.post(request_url, payload).json()

                        if make_comment['meta']['code'] == 200:
                            print "Successfully Posted Targetted Comment!"
                if 'pizza' in caption or 'PIZZA' in caption:

                    print 'Read Caption: %s' % (caption)
                    media_id = get_post_id(insta_username)
                    comment_text="Dominoz is discounting upto 50% rates in pizza this week.checkout best price for" \
                                 "you at www.vishavmarkets.com.Best prices of BADDI"
                    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
                    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
                    print 'POST request url : %s' % (request_url)

                    make_comment = requests.post(request_url, payload).json()

                    if make_comment['meta']['code'] == 200:
                        print "Successfully Posted Targetted Comment!"
                else:
                    print 'There is no caption on the post!'

        else:

            print 'Status code other than 200 received!'
target_caption_comments(insta_username)