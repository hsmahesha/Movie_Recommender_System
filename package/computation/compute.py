#------------------------------------------------------------------------------#
# import required python modules here                                          #
#------------------------------------------------------------------------------#
import math
import numpy as np
from numpy import *
#------------------------------------------------------------------------------#



#------------------------------------------------------------------------------#
# compute cosine similarity between two vectors                                #
#------------------------------------------------------------------------------#
def cosine_similarity(v1, v2):

  return np.dot(v1, v2) / (np.sqrt(np.dot(v1, v1)) * np.sqrt(np.dot(v2, v2)))
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# compute k nearest neighbors of user-id                                       #
#------------------------------------------------------------------------------#
def k_nearest_neighbors_of_user_id(mat, n_users, user_id, knn):

  u_dict = {}
  r = 0
  uid_row = mat[user_id]
  for row in mat:
    if user_id != r:
      cs = cosine_similarity(uid_row, row)
      u_dict[r] = cs
    r += 1
  u_dict = sorted(u_dict.items(), key = lambda arg: arg[1], reverse = True)
  u_dict = u_dict[0:knn]

  knn_list = []
  for k, v in u_dict:
    knn_list.append(k)

  return knn_list
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# compute top n movies which can be recommended to user-id
#------------------------------------------------------------------------------#
def top_n_movies_for_user_id(mat, n_rows, n_cols, top_n, knn_list):

  movie_arr = np.zeros(n_cols)
  for k in knn_list:
    movie_arr = np.add(movie_arr, mat[k])

  m_dict = {}
  for i in range(0, n_cols):
    m_dict[i] = movie_arr[i]

  m_dict = sorted(m_dict.items(), key = lambda arg: arg[1], reverse = True)
  m_dict = m_dict[0:top_n]

  top_n_list = []
  for k, v in m_dict:
    top_n_list.append(k)
  return top_n_list
#------------------------------------------------------------------------------#
