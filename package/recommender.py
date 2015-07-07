################################################################################
#                                                                              #
#        Interface To Different Movie Recommendation Systems                   #
#                                                                              #
################################################################################



#------------------------------------------------------------------------------#
# import required built-in python modules here                                 #
#------------------------------------------------------------------------------#
import os
import sys                                                                     #
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# import recommender related  python modules here                              #
#------------------------------------------------------------------------------#
import package.recommenders.svd_recommender.svd_recom as svd
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# import classes and other stuffs from above modules                           #
#------------------------------------------------------------------------------#
from package.recommenders.svd_recommender.svd_recom import *
#------------------------------------------------------------------------------#



#------------------------------------------------------------------------------#
# public interface to different movie recommendation systems. call different   #
# recommendation systems based on user input.                                  #                    
#------------------------------------------------------------------------------#
def recommend(movie_data):
  svd_recommender = svd.SVDRecommmender(movie_data)
  recommended_list = svd_recommender.recommend()
  return recommended_list
#------------------------------------------------------------------------------#
