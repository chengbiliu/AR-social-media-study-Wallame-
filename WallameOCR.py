import csv
import pandas as pd
import os
import gc
import io

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types as type1
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types as type2

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\Chengbi\\OneDrive - George Mason University\\Research\\WebScraper\\newkey.json"

def detect_text(path):
    """Detects text in the file."""
    imgclient = vision.ImageAnnotatorClient()
    nlpclient = language.LanguageServiceClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = type1.Image(content=content)
    response = imgclient.text_detection(image=image)
    texts = response.text_annotations
    if len(texts) != 0:
        for text in texts:
            textcontent = text.description
            textlanguage = text.locale
            document = type2.Document(
                content=text.description,
                type=enums.Document.Type.PLAIN_TEXT)
            # Detects the sentiment of the text
            try:
                sentiment = nlpclient.analyze_sentiment(document=document).document_sentiment
                sentimentscore = sentiment.score
                sentimentmagnitude = sentiment.magnitude
            except:
                sentimentscore = 'N/A1'
                sentimentmagnitude = 'N/A1'
            break
    else:
        textcontent = 'N/A'
        textlanguage = 'N/A'
        sentimentscore = 'N/A'
        sentimentmagnitude = 'N/A'

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
    return textcontent, textlanguage, sentimentscore, sentimentmagnitude

def detect_box(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
        
#    print('Texts:')
    
    boxes=[]
    for text in texts:
#        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

#        print('bounds: {}'.format(','.join(vertices)))
        boxes.append(vertices)
    return boxes

try:
    df = pd.read_csv('HasText(unclean).csv', encoding='utf-8')
except:
    df = pd.read_csv('HasText(unclean).csv', encoding='latin-1')

## parse latlon and time
#df1 = df['latlon'].str.split(',', expand=True)
#df1[0]=df1[0].str.replace("{","").str.replace('"latitude": ',"")
#df1[1]=df1[1].str.replace("}","").str.replace('"longitude": ',"")
#df1.columns=['latitude','longitude']
#df2 = df['time'].str.split('T', expand=True)
#df2[1]=df2[1].str.replace("Z","")
#df2['hour']=df2[1].str[:2]
#df2.columns=['date','fulltime','hour']
#df3 = pd.concat([df, df1, df2], axis=1, join_axes=[df.index])
#df = df3.drop(['latlon','time'],axis=1)

i=0
for item in df.picurl:
    data=[]
    data1=[]
    boxresult = detect_box("C:\\Users\\Chengbi\\OneDrive - George Mason University\\Research\\WebScraper\\images\\{0}.png".format(item[-10:]))
    imgresult = detect_text("C:\\Users\\Chengbi\\OneDrive - George Mason University\\Research\\WebScraper\\images\\{0}.png".format(item[-10:]))
    data.append(imgresult)
    data1.append(boxresult)
    dfresults = pd.DataFrame(data)
    dfresults1 = pd.DataFrame(data1)
#    print (dfresults)
#    dfall = pd.concat([df, dfresults], axis=1, join_axes=[df.index])
    dfresults.to_csv('outtexta.csv',mode='a',encoding='utf-8',header="false")
    dfresults1.to_csv('outboxa.csv',mode='a',encoding='utf-8',header="false")
#    dfresults.to_json('outbox.json',orient="split")
    del dfresults
    del dfresults1
    del data
    del data1
    gc.collect()
    i+=1
    print(i)
    print(item)
    #break
#    input("Press Enter to continue...")
    

