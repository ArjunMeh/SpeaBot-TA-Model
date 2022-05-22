from requests_html import HTMLSession
from rake_nltk import Rake
import nltk

def mark(file_path):
    
    f = open(file_path,encoding='utf8')
    text =  f.read()
    r = Rake()
    r.extract_keywords_from_text(text)
    for rating, keyword in r.get_ranked_phrases_with_scores():
        if rating > 5:
            rating =  "{:.2f}".format(rating)
            print(rating, keyword)