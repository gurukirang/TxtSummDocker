import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
text = """There was very little to separate Gujarat Giants and Royal Challengers Bangalore last season, with both teams finishing at the bottom of the table with two wins each in eight games.

It's still early days in the 2024 edition of the Women's Premier League and they have started out in contrasting fashion. While RCB edged out UP Warriorz in a last ball finish to make a winning start in this season, Gujarat Giants were outplayed by Mumbai Indians. In a tournament where games have gone down to last-ball finishes, Giants have been the only laggards in the pack."""

def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    #print (stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    #print (doc)
    tokens =[token.text for token in doc]
    # print(tokens)
    word_freq ={}
    for word in doc :
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text] += 1

    # print (word_freq)

    max_freq = max (word_freq.values())
    # print(max_freq)                

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

    # print(word_freq)      
            
    sent_tokens = [sent for sent in doc.sents]
    # print(sent_tokens)          

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]

    print(sent_scores)                

    select_len = int(len(sent_tokens)*0.3) 
    # print(select_len)               
    summary = nlargest(select_len, sent_scores, key =sent_scores.get)
    # print(summary)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    # print(text)
    # print(summary)
    # print("length of original text ",len(text.split(' ')))
    # print("length of summary text ",len(summary.split(' ')))

    return summary,doc,len(rawdocs.split(' ')), len(summary.split(' '))
