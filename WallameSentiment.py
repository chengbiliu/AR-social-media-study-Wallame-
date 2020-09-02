import csv
import pandas as pd
import os
import gc

# Imports the Google Cloud client library

from google.cloud import language
from google.cloud.language import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\Chengbi\\OneDrive - George Mason University\\Research\\WebScraper\\newkey.json"

def detect_sentiment(text):
    """Detects text in the file."""
    nlpclient = language.LanguageServiceClient()
    if len(text) != 0:
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)
        sentiment = nlpclient.analyze_sentiment(document=document).document_sentiment
        sentimentscore = sentiment.score
        sentimentmagnitude = sentiment.magnitude
#    except:
#        sentimentscore = 'N/A1'
#        sentimentmagnitude = 'N/A1'

    # detect labels in picture
#    response1 = imgclient.label_detection(image=image)
#    labels = response1.label_annotations
#    if len(labels) != 0:
#        for label in labels:
#            labeldescription=label.description
#            labeltopicality=label.topicality
#            break
#    else:
#        labeldescription = 'N/A'
#        labeltopicality = 'N/A'

    # detect image properties (e.g., rgb, dominant color, etc.)
#    response2 = imgclient.image_properties(image=image)
#    props = response2.image_properties_annotation
#    lista=[]
#    for c in props.dominant_colors.colors:
#        lista.append(c.pixel_fraction)
#    dominantcolorperc = max(lista)
#    redtotal = 0
#    greentotal = 0
#    bluetotal = 0
#    for c in props.dominant_colors.colors:
#        # return dominant color's rgb
#        if c.pixel_fraction == dominantcolorperc:
#            reddom = c.color.red
#            greendom = c.color.green
#            bluedom = c.color.blue
#        redtotal += c.color.red * c.pixel_fraction
#        greentotal += c.color.green * c.pixel_fraction
#        bluetotal += c.color.blue * c.pixel_fraction
    return sentimentscore, sentimentmagnitude

try:
    df = pd.read_csv('Mason.csv', encoding='utf-8')
except:
    df = pd.read_csv('Mason.csv', encoding='latin-1')
    
for item in df.textcontent:
    print(item)
    data=[]
    sentimentresult = detect_sentiment(item)
    data.append(sentimentresult)
    dfresults = pd.DataFrame(data)
#    print (dfresults)
#    dfall = pd.concat([df, dfresults], axis=1, join_axes=[df.index])
    dfresults.to_csv('outsentiment.csv',mode='a',encoding='utf-8',header="false")