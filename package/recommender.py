################################################################################
#                                                                              #
#        Interface To Different Movie Recommendation Systems                   #
#                                                                              #
################################################################################



#------------------------------------------------------------------------------#
# import required built-in python modules here                                 #
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# import recommender related  python modules here                              #
#------------------------------------------------------------------------------#
import package.recommenders.svd_recommender.svd_recom as svd
import package.recommenders.pear_corr_recommender.pcc_recom as pcc
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# import classes and other stuffs from above modules                           #
#------------------------------------------------------------------------------#
from package.recommenders.svd_recommender.svd_recom import *
from package.recommenders.pear_corr_recommender.pcc_recom import *
#------------------------------------------------------------------------------#



#------------------------------------------------------------------------------#
# public interface to different movie recommendation systems. call different   #
# recommendation systems based on user input.                                  #                    
#------------------------------------------------------------------------------#
def recommend(data):
  svd_recommender = svd.SVDRecommmender(data)
  recommended_list = svd_recommender.recommend()
  #pcc_recommender = pcc.PCCRecommender(data)
  #recommended_list = pcc_recommender.recommend()
  return recommended_list
#------------------------------------------------------------------------------#
