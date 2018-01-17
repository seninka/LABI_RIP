def filter_tweets(tweets, followers_count_limit):
    filtered = []
    for tweet in tweets:
            if tweet[ 'user' ][ 'followers_count' ] >= followers_count_limit:
                filtered.append(tweet)
    return filtered
all_tweets = [{
'user' : {
'name' : 'vasja' ,
'followers_count' : 1189 ,
},
'text' : 'hello, world'
}, {
'user' : {
'name' : 'petja' ,
'followers_count' : 20 ,
},
'text' : 'some message'
}]
# call our function
filtered_tweets = filter_tweets(all_tweets, 100 )
print ( 'Filtered tweets: ' )
print (filtered_tweets)
