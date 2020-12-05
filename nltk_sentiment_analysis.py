import re
import nltk
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import GetOldTweets3 as got
from collections import Counter
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def tweet_generator():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('TheRock')\
        .setSince("2020-05-23")\
        .setUntil("2020-07-23")\
        .setMaxTweets(100)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    tweet_list = [tweet.text for tweet in tweets]
    return tweet_list
# with open('read.txt', encoding='charmap') as f:
#     text = f.read()


tweets_text = tweet_generator()
length_of_tweet_list = len(tweets_text)
tweets_text_string = ""
while(length_of_tweet_list > 0):
    tweets_text_string = tweets_text[length_of_tweet_list-1] + \
        " "+tweets_text_string
    length_of_tweet_list -= 1


lower_case_text = tweets_text_string.lower()
cleaned_text = re.sub(r"\W+|_", " ", lower_case_text)
cleaned_text_list = word_tokenize(cleaned_text, 'english')

tokened_list = [
    word for word in cleaned_text_list if not word in stopwords.words('english')]


emotions_list = []
with open('emotions.txt') as f:
    for line in f:
        cleaned_text_line = re.sub(r"[/\n,']", "", line).strip()
        word, emotions = cleaned_text_line.split(':')
        if word in tokened_list:
            emotions_list.append(emotions)
w = Counter(emotions_list)


def sentiment_anlaysis(snetiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(snetiment_text)
    print(score)
    negative = score['neg']
    positive = score['pos']
    if negative > positive:
        print("The Rock is negative with his thoughts")
    elif positive > negative:
        print("The Rock is positive with his thoughts")

    else:
        print("The Rock is neutral")


sentiment_anlaysis(cleaned_text)


fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
