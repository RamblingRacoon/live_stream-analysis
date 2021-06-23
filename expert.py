import os
from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()
import json

def sentiment(data_input):
    language= 'en'
    total_sentiment = 0
    average_sentiment = []
    each_message_sentiments = []
    with open(data_input, 'r', encoding ='utf8') as f:
        json_obj = json.load(f)
        for idx, post_id in enumerate(json_obj.keys()):
            post  = json_obj[post_id]
            text = post["message_body"]
            output = client.specific_resource_analysis(
                body={"document": {"text": text}}, 
                params={'language': language, 'resource': 'sentiment'
            })
            sentiment_score = output.sentiment.overall
            total_sentiment += sentiment_score
            average_sentiment.append("{:.2f}".format(total_sentiment/(idx+1)))
            each_message_sentiments.append("{:.2f}".format(sentiment_score))

    sentiment={
        "average_sentiment": average_sentiment,
        "each_message_sentiments": each_message_sentiments
    }  
    return sentiment

def concepts(data_input):
    collection_of_concepts = {}
    lang = "en"
    with open(data_input, 'r', encoding ='utf8') as f:
        json_obj = json.load(f)
        for post_id in json_obj.keys():
            post  = json_obj[post_id]
            text = post["message_body"]
            document = client.specific_resource_analysis(
            body={"document": {"text": text}}, 
            params={'language': lang, 'resource': 'relevants'})

            for main_concept in document.main_syncons:
                collection_of_concepts[main_concept.lemma] = collection_of_concepts.get(main_concept.lemma, 0)+1
    collection_of_concepts = dict(sorted(collection_of_concepts.items(), key=lambda item: item[1], reverse=True))    
    return collection_of_concepts


data_file = "data_sm.json"
if os.path.exists("concepts.json"):
    with open("concepts.json", 'r', encoding ='utf8') as f:
        collection_of_concepts = json.load(f)
else:
    collection_of_concepts = concepts(data_file)
    with open("concepts.json", 'w', encoding ='utf8') as f:
        json.dump(collection_of_concepts, f, indent=4)

if os.path.exists("sentiment.json"):
    with open("concepts.json", 'r', encoding ='utf8') as f:
        sentiment_data = json.load(f)
else:
    sentiment_data = sentiment(data_file)
    with open("sentiment.json", 'w', encoding ='utf8') as f:
        json.dump(sentiment_data, f, indent=4)
