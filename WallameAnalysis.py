import cv2
import pandas as pd
import numpy as np

# df = pd.read_csv('test.csv',encoding='latin-1')
# features = ['hour','labeltopicality','dominantcolorperc','red','green','blue']
# # Separating out the features
# x = df.loc[:, features].values
# # Separating out the target
# y = df.loc[:,['sentimentscore']].values
#
# # Standardizing the features
# x = StandardScaler().fit_transform(x)
#
# pca = PCA(n_components=3)
# principalComponents = pca.fit_transform(x)
# print(pca.explained_variance_ratio_)
# print(pca.components_)
# principalDf = pd.DataFrame(data = principalComponents,columns = ['principal component 1', 'principal component 2', 'principal component 3'])
# finalDf = pd.concat([principalDf, df[['sentimentscore']]], axis = 1)
# finalDf.to_csv('pcaresult.csv',encoding='utf8')

def image_colorfulness(image):
    # split the image into its respective RGB components
    (B, G, R) = cv2.split(image.astype("float"))

    # compute rg = R - G
    rg = np.absolute(R - G)

    # compute yb = 0.5 * (R + G) - B
    yb = np.absolute(0.5 * (R + G) - B)

    # compute the mean and standard deviation of both `rg` and `yb`
    (rbMean, rbStd) = (np.mean(rg), np.std(rg))
    (ybMean, ybStd) = (np.mean(yb), np.std(yb))

    # combine the mean and standard deviations
    stdRoot = np.sqrt((rbStd ** 2) + (ybStd ** 2))
    meanRoot = np.sqrt((rbMean ** 2) + (ybMean ** 2))

    # derive the "colorfulness" metric and return it
    return stdRoot + (0.3 * meanRoot)

try:
    df = pd.read_csv('outbox.csv', encoding='utf-8')
except:
    df = pd.read_csv('outbox.csv', encoding='latin-1')

#data=[]
#i=0
#for item in df.picurl:
#    oldimg = cv2.imread("C:\\Users\\Chengbi\\OneDrive - George Mason University\\Research\\WebScraper\\images\\{0}.png".format(item[-10:]),-1)
#    mask = np.zeros(oldimg.shape, dtype=np.uint8)
#    points = np.array([[(60,220),(577,220),(577,845),(60,845)]],dtype=np.int32)
#    
#    channel_count = oldimg.shape[2]  # i.e. 3 or 4 depending on your image
#    ignore_mask_color = (0,)*channel_count
#    cv2.fillPoly(mask, points, ignore_mask_color)
#    
#    masked_image = cv2.bitwise_and(oldimg, mask)
#   
#    cv2.imshow('img',masked_image)
#    cv2.waitKey(0)
#    aaa = image_colorfulness(masked_image)
#    data.append(aaa)
#    i+=1
#    print(i)
#    print(aaa)
#    break
#dfresults = pd.DataFrame(data, columns=['colorfulness'])
#dfresults.to_csv('color.csv',mode='a',encoding='utf-8',header="false")
