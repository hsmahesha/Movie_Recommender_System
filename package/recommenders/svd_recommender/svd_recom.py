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
  # compute top n movies which can be recommended to user-id                   #
  #----------------------------------------------------------------------------#
  def __top_n_movies_for_user_id(self, knn_list):

    # compute the frequency count of each movie for top k nearest neighbors
    mat = self.__data.um_mat
    n_cols = self.__data.n_cols
    movie_arr = np.zeros(n_cols)
    for k in knn_list:
      movie_arr = np.add(movie_arr, mat[k])

    # create a dictionary from movie frequency count array
    m_dict = {}
    for i in range(0, n_cols):
      m_dict[i] = movie_arr[i]

    # select top n movies for users whose frequency counts is higher
    top_n_list = compute.get_top_n_movies(m_dict, mat, self.__data.user_id, \
                                          self.__data.top_n)
    return top_n_list
  #----------------------------------------------------------------------------#


  #----------------------------------------------------------------------------#
  # compute k nearest neighbors of user-id                                     #
  #----------------------------------------------------------------------------#
  def __k_nearest_neighbors_of_user_id(self, us_mat):

    # compute cosine similarity between user_id and other users
    u_id = self.__data.user_id
    u_dict = {}
    r = 0
    for row in us_mat:
      if u_id != r:
        cs = compute.cosine_similarity(us_mat[u_id], row)
        u_dict[r] = cs
      r += 1

    # sort the users in the decreasing order of their cosine similarity with
    # user-id
    u_dict = sorted(u_dict.items(), key = lambda arg: arg[1], reverse = True)

    # select top k nearest neighbors based on their cosine similarity values
    knn = self.__data.knn
    u_dict = u_dict[0:knn]
    knn_list = []
    for k, v in u_dict:
      knn_list.append(k)

    return knn_list
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
    knn_list = self.__k_nearest_neighbors_of_user_id(us_mat)

    # compute top n movies which can be recommended to user-id
    top_n_list = self.__top_n_movies_for_user_id(knn_list)

    # return recommended top n movies to user-id
    return top_n_list
  #----------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
