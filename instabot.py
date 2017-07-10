from like_a_post import like_a_post
from post_a_comment import post_a_comment
from get_user_post import get_users_post
from get_own_post import get_own_post
from get_user_info import get_user_info
from delete_negative_comment import delete_negative_comment
from get_comment_list import get_comment_list
from get_like_list import get_like_list
from self_info import self_info
from colorama import init
from colorama import Fore,Back,Style
from trending import get_trending_tag_counts
init()

show_menu = True
while show_menu:
    print(Fore.GREEN+Style.BRIGHT+"---------------WELCOME TO SMARTER INSTABOT APPLICATION--------------------")
    print(Fore.BLUE+Style.BRIGHT+"\n..............WE ARE HAPPY TO GIVE YOU OUR SERVICES............\n")
    print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+".......MAKE YOUR LIFE EASY HERE........")
    print "\n"
    print Fore.GREEN+Style.BRIGHT+"Here are your menu options:"
    print "1.Get your own details\n"
    print "2.Get details of a user by username\n"
    print "3.Get your own recent post\n"
    print "4.Get the recent post of a user by username\n"
    print "5.Get a list of people who have liked the recent post of a user\n"
    print "6.Like the recent post of a user\n"
    print "7.Get a list of comments on the recent post of a user\n"
    print "8.Make a comment on the recent post of a user\n"
    print "9.Get Trending Tags and counts\n"
    print "10.Delete negative comments from the recent post of a user\n"
    print "11.Exit"
    Style.RESET_ALL

    menu_choice = raw_input("Now Kindly Enter Your Choice\n")
    if (menu_choice) > 0:
        menu_choice = int(menu_choice)

        if menu_choice == 1:
            print "You Have Chosen option To Get Your Information\n"
            print "Following Are Your Details"
            self_info()

        elif menu_choice == 2:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"wait work under process.......")
            get_user_info(insta_username)
            print (Style.RESET_ALL)
            print("\n")

        elif menu_choice == 3:
            print (Fore.GREEN+Style.BRIGHT+"WAit Getting ur post.......\n")
            get_own_post()
            print "Your image has been downloaded!....to.....C:\Users\GUPTA\PycharmProjects\instabot\\"
            print (Style.RESET_ALL)
            print("\n")

        elif menu_choice == 4:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait Downloading user post......")
            get_users_post(insta_username)
            print "Your image has been downloaded!....to.....C:\Users\DELL\PycharmProjects\instabot\\"
            print (Style.RESET_ALL)
            print("\n")

        elif menu_choice == 5:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait getting information.....")
            get_like_list(insta_username)
            print (Style.RESET_ALL)
            print("\n")

        elif menu_choice ==6:
            insta_username = raw_input(Fore.RED + Style.BRIGHT + "Enter Username.........\n")
            print(Fore.GREEN + Style.BRIGHT + "Wait liking Ur POst......")
            like_a_post(insta_username)
            print(Style.RESET_ALL)
            print("\n")

        elif menu_choice ==7:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print("\n"+Fore.GREEN+Style.BRIGHT+"Wait getting information.....\n")
            get_comment_list(insta_username)

        elif menu_choice == 8:
            insta_username = raw_input(Fore.BLUE+Style.BRIGHT+"Enter the username of the user: ")
            print(Fore.GREEN+Style.BRIGHT+"Wait Posting A Comment Is Under PROCESS")
            post_a_comment(insta_username)

        elif menu_choice == 9:
            tag = raw_input(Fore.RED+Style.BRIGHT+"Enter Tagname.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait counting Ur Tags......")
            get_trending_tag_counts(tag)
            print(Style.RESET_ALL)
            print("\n")
            print("\n")

        elif menu_choice == 10:
            insta_username = raw_input(Fore.RED + Style.BRIGHT + "Enter Username.........\n")
            print("\n" + Fore.GREEN + Style.BRIGHT + "Progress Is In Deletion.\n")
            delete_negative_comment(insta_username)
            print (Style.RESET_ALL)
            print("\n")

        else:
            show_menu = False