import requests
from constants import APP_ACCESS_TOKEN ,BASE_URL
from get_user_post import get_users_post
from colorama import *
init()
import matplotlib.pyplot as plt

#this method is used to get a count of a particular trending tag taken from the user and also telling
#whether a particular tag is in trend or not based upon applied conditions
#after that this method is also able to plot this data on the X-Y axis on the graph
def get_trending_tag_counts(tag) :
    request_url = (BASE_URL + "tags/" + tag + "?access_token=" + APP_ACCESS_TOKEN)
    get_a_comment = requests.get(request_url).json()
    if get_a_comment['meta']['code'] == 200:
        print(Fore.CYAN+Style.BRIGHT+"Here is your tag...Popularity\n")
        print(Fore.GREEN+Style.BRIGHT+">>> "+str(get_a_comment['data']['media_count'])+" <<<")
        if int(get_a_comment['data']['media_count'])>10000 :
            print "This tag is more popular and is in much trend"
        else:
            print "Tag is Becoming popular with a speed but not so much popular"
        plt.plot(get_a_comment['data']['media_count'], 'ro')
        plt.axis()
        plt.ylabel('Trending----->')
        plt.xlabel("Insta-Bot")
        plt.show()
        print (Style.RESET_ALL)
        return True
    else:
        print(Fore.RED+Style.BRIGHT+'not successful')


#get_trending_tag_counts("modi")