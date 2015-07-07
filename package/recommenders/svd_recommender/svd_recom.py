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
  __k = None
  __knn = None
  __us_mat = None
  __svt_mat = None
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # special init method to initialize an object of type 'SVDRecommender'       #
  #----------------------------------------------------------------------------#
  def __init__(self, data):
    self.__data = data
    self.__k = int(14)
    self.__knn = int(14)
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # compute top n movies which can be recommended to user-id
  #----------------------------------------------------------------------------#
  def __compute_top_n_movies(self, u_dict):

    movie_arr = np.zeros(self.__data.n_cols)
    c_dict = u_dict[self.__data.user_id-1]  # cosine similarity of user i is
                                            # recorded in loc i-1
    for k, v in c_dict:
       movie_arr = np.add(movie_arr, self.__data.um_mat[k])

    m_dict = {}
    for i in range(0, self.__data.n_cols):
      m_dict[i] = movie_arr[i]

    m_dict = sorted(m_dict.items(), key = lambda arg: arg[1], reverse = True)
    m_dict = m_dict[0:self.__data.top_n]

    top_n_list = []
    for k, v in m_dict:
       top_n_list.append(k+1) # we need to add 1, because 0th col corresponds
                              # movie 1, etc 
    return top_n_list
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # compute k nearest neighbors of each user                                   #
  #----------------------------------------------------------------------------#
  def __k_nearest_neighbor_users(self):

    u_dict = {}
    for i in range(0, self.__data.n_rows):
      r = 0
      c_dict = {}
      for row in self.__us_mat:
        if i != r:
          cs = compute.cosine_similarity(self.__us_mat[i], row)
          c_dict[r] = cs
        r += 1
      c_dict = sorted(c_dict.items(), key = lambda arg: arg[1], reverse = True)
      c_dict = c_dict[0:self.__knn]
      u_dict[i] = c_dict

    return u_dict
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # factorize the um-matrix using svd decomposition                            #
  #----------------------------------------------------------------------------#
  def __svd_decomposition(self):

    # svd decomposition
    u_mat, s_arr, vt_mat = np.linalg.svd(self.__data.um_mat)

    # retain only first k columns of u_mat and chop rest of the columns
    u_mat = np.delete(u_mat, s_[self.__k:], axis=1)

    # retain only first k rows of vt_mat and chop rest of the rows. 
    vt_mat = np.delete(vt_mat, s_[self.__k:], axis=0)

    # retain only first k singular values
    s_arr = s_arr[:self.__k]

    # get a k x k diagonal matrix from first k singular values
    s_mat = np.diag(s_arr)

    # get sqrt of s_mat
    s_mat = np.sqrt(s_mat)

    # compute dot product of u_mat and s_mat
    self.__us_mat = np.dot(u_mat, s_mat)

    # compute dor product of s_mat and vt_mat
    self.__svt_mat = np.dot(s_mat, vt_mat)
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
    self.__svd_decomposition()

    # compute k nearest neighbors for each user
    u_dict = self.__k_nearest_neighbor_users()

    # compute top n movies which can be recommended to user-id
    top_n_list = self.__compute_top_n_movies(u_dict)

    # return recommended top n movies to user-id
    return top_n_list
  #----------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
