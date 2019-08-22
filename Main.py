# Brandon Arbuthnot
# CSE 5914

# Import libraries
import tweepy
import random
import config

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

########################################## Function Definitions ####################################################

# Splash Screen
def splash():
    print('*****************************************')
    print('**  [Welcome to: Lost In Translation]  **')
    print('*****************************************')
    print('LiT, the social media translation game by Brandon Arbuthnot and Ben Memberg\n')
    start()

# Primary game function
def start():
    # Difficulty variable
    k = 3
    j = 20

    # Retrieve User input twitter handle
    id_list = prompt_pool()

    # Narrow choices from pool
    sampling = random.sample(id_list, k)

    # Translate Twitter id to name
    user_list = [api.get_user(id).name for id in sampling]

    # Pick the tweeter
    answer = random.choice(sampling)
    tweet_set = (api.user_timeline(answer, count = j, tweet_mode = 'extended', include_rts = False))

    # This is the text version of the tweet to be translated
    tweet_text = str(random.choice(tweet_set).full_text.encode('ascii', 'ignore'))

    # print("How many times would you like the tweet to be lost in translation? (Enter a number 1-10):")
    # z = input()
    # translate_func(tweet_text, z)

    print('************** [The Tweet] ***************\n\"' + tweet_text + '\"\n******************************************')
    print('Whose tweet was this? (Enter a number 1-' + str(k) + ')')

    # Display tweet candidates
    for user in user_list:
        print((str(user_list.index(user) + 1)) + '. ' + user)

    # Player answer
    player_guess = input()

    # Answer checking
    if (player_guess-1 == sampling.index(answer)):
        print("Nicely done! This was " + api.get_user(answer).name + "'s tweet.")
    else:
        print("Wrong! This was actually " + api.get_user(answer).name + "'s tweet.")

    # Reset
    reset_prompt()

# prompt for pool of followed accounts (aka 'friends')
def prompt_pool():
    print('Please enter a Twitter Handle (ex: user_handle1) to play:')
    user = raw_input()
    if (user == ''): user = 'cse5914'
    return api.friends_ids(user)

# Play again? prompt
def reset_prompt():
    print("Would you care to play again? Y/n")
    user_in = raw_input()
    if (user_in.lower() == 'y'): start()

#################################################### Main execution ########################################################
splash()