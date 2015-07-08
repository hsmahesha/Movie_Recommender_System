################################################################################
#                                                                              #
#                         SVD Based Movie Recommender:                         #
#                                                                              #
# The SVD based movie recommender is based on the paper following paper        #
# http://files.grouplens.org/papers/webKDD00.pdf                               #
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
class SVDRecommmender:

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
  # factorize the um-matrix using svd decomposition                            #
  #----------------------------------------------------------------------------#
  def __svd_decomposition(self):

    # svd decomposition
    u_mat, s_arr, vt_mat = np.linalg.svd(self.__data.um_mat)

    # decide on the number of singular values to be retained
    k = int(14)

    # retain only first k columns of u_mat and chop rest of the columns
    u_mat = np.delete(u_mat, s_[k:], axis=1)

    # retain only first k rows of vt_mat and chop rest of the rows. 
    vt_mat = np.delete(vt_mat, s_[k:], axis=0)

    # retain only first k singular values
    s_arr = s_arr[:k]

    # get a k x k diagonal matrix from first k singular values
    s_mat = np.diag(s_arr)

    # get sqrt of s_mat
    s_mat = np.sqrt(s_mat)

    # compute dot product of u_mat and s_mat
    us_mat = np.dot(u_mat, s_mat)

    # return us_mat
    return us_mat
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # replace all non-zero values in the user-movie matrix to 1                  #
  #----------------------------------------------------------------------------#
  def __replace_non_zero_with_one(self):

    for r in range(0, self.__data.n_rows):
      for c in range(0, self.__data.n_cols):
        if self.__data.um_mat[r, c] != 0:
          self.__data.um_mat[r, c] = 1
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # public interface method of 'class MovieRecommender'                        #
  #----------------------------------------------------------------------------#
  def recommend(self):

    # replace all non-zero ratings by 1
    self.__replace_non_zero_with_one()

    # factorize the um-matrix using svd decomposition
    us_mat = self.__svd_decomposition()

    # compute k nearest neighbors for user-id
    knn_list = compute.k_nearest_neighbors_of_user_id( \
               us_mat, self.__data.n_rows, self.__data.user_id, self.__data.knn)

    # compute top n movies which can be recommended to user-id
    top_n_list = compute.top_n_movies_for_user_id(self.__data.um_mat, \
                 self.__data.n_rows, self.__data.n_cols, self.__data.top_n, \
                 knn_list)

    # return recommended top n movies to user-id
    return top_n_list
  #----------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
