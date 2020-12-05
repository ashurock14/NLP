import GetOldTweets3 as got
import re
from collections import Counter
import matplotlib.pyplot as plt


def tweet_generator():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus')\
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


print(tweets_text_string)

# with open('read.txt', 'w', encoding='charmap') as f:
#     f.write(tweets_text_string)

lower_case_text = tweets_text_string.lower()


cleaned_text = re.sub(r"\W+|_", " ", lower_case_text)
# with open('read.txt', 'w') as f:
#     f.write(cleaned_text)
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list


cleaned_text_list = cleaned_text.split(" ")
tokened_list = [word for word in cleaned_text_list if not word in stop_words]


emotions_list = []
with open('emotions.txt') as f:
    for line in f:
        cleaned_text_line = re.sub(r"[/\n,']", "", line).strip()
        word, emotions = cleaned_text_line.split(':')
        if word in tokened_list:
            emotions_list.append(emotions)
w = Counter(emotions_list)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
