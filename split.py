import pickle
import requests
import math

# Load the image features
img_features = pickle.load(open('image_features_embeddingWOMEN3.pkl', 'rb'))
start = 0
clutter_size = math.ceil(len(img_features)/66)

for i in range(66):
    pickle.dump(img_features[start:(i+1)*clutter_size], open('img_data\\files\\image_features_embeddingWOMEN{}.pkl'.format(i), 'wb'))

    print(i)
    
    start = (i+1)*clutter_size 