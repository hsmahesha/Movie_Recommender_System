################################################################################
#                                                                              #
#              Pearson Correlation Based Movie Recommender:                    #
#                                                                              #
################################################################################
#                                                                              #
# This file implements the pearson correlation icoefficient based movie        #
# recommender syhstem.                                                         #
#                                                                              #
# Note: This is a work in progress code. it is not tested thoroughly           #
#                                                                              #
################################################################################




#------------------------------------------------------------------------------#
# import required built-in python modules here                                 #
#------------------------------------------------------------------------------#
import sys
import math
import numpy as np
from numpy import *
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# add path to movie recommender package before importing modules from this     #
# package                                                                      #
#------------------------------------------------------------------------------#
sys.path.insert(0, "./package")
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# import required package modules here                                         #
#------------------------------------------------------------------------------#
import package.computation.compute as compute
#------------------------------------------------------------------------------#




#------------------------------------------------------------------------------#
# class SVDRecommmender: This class implements the svd based movie recommen-   #
# -dation system.                                                              #
#------------------------------------------------------------------------------#
class PCCRecommender:

  #----------------------------------------------------------------------------#
  # private data members
  #----------------------------------------------------------------------------#
  __data = None
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # special init method to initialize an object of type 'SVDRecommender'       #
  #----------------------------------------------------------------------------#
  def __init__(self, data):
    self.__data = data
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # compute top n movies which can be recommended to user-id                   #
  #----------------------------------------------------------------------------#
  def __top_n_movies_for_user_id(self, knn_dict):

    # compute the predicted ratings of user_id for each movie, and select top
    # n movies which have got higher prediction ratings.
    mat = self.__data.um_mat
    n_cols = self.__data.n_cols
    mat_t = np.matrix.transpose(mat)
    m = 0
    m_dict = {}
    for movie in mat_t:
      pr = 0.0
      for u, v in knn_dict:
        pr += (movie[u] * v)
      m_dict[m] = pr
      m += 1

    top_n_list = compute.get_top_n_movies(m_dict, mat, self.__data.user_id, \
                                          self.__data.top_n)
    return top_n_list
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # compute k nearest neighbors of user-id                                     #
  #----------------------------------------------------------------------------#
  def __k_nearest_neighbors_of_user_id(self, p_dict):

    # compute the influence of each different users based on thier pearson 
    # correlation values
    pcc_sum = 0.0
    for item in p_dict.items():
      pcc_sum += item[1]

    cr_dict = {}
    for item in p_dict.items():
      k = item[0]
      v = item[1]
      cr_dict[k] = v / pcc_sum

    # sort the users in the decreasing order of their influence, and select
    # top k influencual users as k nearest neighbors
    cr_dict = sorted(cr_dict.items(), key = lambda arg: arg[1], reverse = True)
    knn = self.__data.knn
    knn_dict = cr_dict[0:knn]

    return knn_dict
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # compute pearson correlation coefficient of user-id with others
  #----------------------------------------------------------------------------#
  def __pearson_correlation(self):

    uid = self.__data.user_id
    mat = self.__data.um_mat
    n_rows = self.__data.n_rows
    n_cols = self.__data.n_cols

    p_dict = {}

    sum_x = np.sum(mat[uid])
    sum_x2 = np.sum(np.square(mat[uid]))

    for r in range(0, n_rows):
      if uid != r:
        sum_y = np.sum(mat[r])
        sum_y2 = np.sum(np.square(mat[r]))
        sum_xy = np.dot(mat[uid], mat[r])

        den = (np.sqrt(sum_x2 - (np.square(sum_x) / n_cols))) * \
              (np.sqrt(sum_y2 - (np.square(sum_y) / n_cols)))
        num = sum_xy - ((sum_x * sum_y) / n_cols)

        if den == 0.0:
          p_dict[r] = float(-1.0)
        else:
          p_dict[r] = float(num / den)

    return p_dict
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # public interface method of 'class MovieRecommender'                        #
  #----------------------------------------------------------------------------#
  def recommend(self):

    # compute pearson correlation coefficient of user-id with others
    p_dict =  self.__pearson_correlation()

    # compute k nearest neighbors for user-id
    knn_dict = self.__k_nearest_neighbors_of_user_id(p_dict)

    # compute top n movies which can be recommended to user-id
    top_n_list = self.__top_n_movies_for_user_id(knn_dict)

    # return recommended top n movies to user-id
    return top_n_list
  #----------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
