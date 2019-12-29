import tweepy, time

# Getting Twitter Developer Keys
consumer_key = "ENTER HERE"
consumer_secret = "ENTER HERE"
access_token = "ENTER HERE"
access_secret = "ENTER HERE"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Create API object
api = tweepy.API(auth)

# Get UserID & FollowerCount
user = api.get_user(TWITTER USER NUMBER ID)
FollowCount = user.followers_count

# Set Follower Goal
goal = 20000

# While Loop to Reach Goal and Update Status
while followCount <= goal * 2:
    if followCount >= goal:
        api.update_status("I got to " + str(followCount) + " Followers!")
        break
    else:
        print(followCount)
        time.sleep(100)

