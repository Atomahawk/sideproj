# MovieRecommender.py
###########################
# collaborative systems recommend based on other similar users likes
# content based systems recommend based on your past likes
# the method we're using is a hybrid

# install dependencies
conda install numpy # for maths
conda install scipy # for maths
conda install lighttpd # for recommendation algorithms

# import dependencies
import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import lightFM 

# fetch data and format it
data = fetch_movielens(min_ratings = 4.0)

# print training and testing data
print(repr(data['train']))
print(repr(data['test']))

#create model:  Weighted Approximate-Rank Pairwise
# warp creates recommendations using existing user rating pairs
# uses gradient descent to iteratively improve weights and
# improve predictions over time
model = lightFM(loss='warp')

#train model
#fit method takes in the data set to train on
	# how many epochs (iterations) to 
	# number of threads (parallel computations)
model.fit(data['train'], epochs=30, num_threads=2)

#generate recommendations
def sample_recommendation(model, data, user_ids):

Finish @4:34:
https://www.youtube.com/watch?v=9gBC9R-msAk&index=3&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU