################################################################################
#                                                                              #
#        Interface To Different Movie Recommendation Systems                   #
#                                                                              #
################################################################################



#------------------------------------------------------------------------------#
# import required built-in python modules here                                 #
#------------------------------------------------------------------------------#
import os
import sys
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# import recommender related  python modules here                              #
#------------------------------------------------------------------------------#
import package.recommenders.svd_recommender.svd_recom as svd
import package.recommenders.pear_corr_recommender.pcc_recom as pcc
import package.utility.util as util
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# import classes and other stuffs from above modules                           #
#------------------------------------------------------------------------------#
from package.recommenders.svd_recommender.svd_recom import *
from package.recommenders.pear_corr_recommender.pcc_recom import *
from package.utility.util import *
#------------------------------------------------------------------------------#



#------------------------------------------------------------------------------#
# public interface to different movie recommendation systems. call different   #
# recommendation systems based on user input.                                  #                    
#------------------------------------------------------------------------------#
def recommend(data):

  # call the recommender system of user choice, and get the output list of
  # top n movies to be recommended
  recommended_list = []
  if data.choice == RSKind.svd:
    svd_recommender = svd.SVDRecommmender(data)
    recommended_list = svd_recommender.recommend()
  elif data.choice == RSKind.pcc:
    pcc_recommender = pcc.PCCRecommender(data)
    recommended_list = pcc_recommender.recommend()

  # return top n movie list to be recommended
  return recommended_list
#------------------------------------------------------------------------------#
