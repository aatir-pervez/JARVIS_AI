import feedparser
from core.speak import speak

def get_news():
    try:
        url = "http://feeds.bbci.co.uk/news/rss.xml"
        feed = feedparser.parse(url)

        speak("Here are the latest news headlines")

        for entry in feed.entries[:5]:
            print("News:", entry.title)
            speak(entry.title)

    except Exception as e:
        print("News error:", e)
        speak("Sorry, I couldn't fetch the news")