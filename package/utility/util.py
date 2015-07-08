################################################################################
#                                                                              #
#                            Utility Module:                                   #
#                                                                              #
################################################################################
#                                                                              #
#   This module implements the different utility functions                     #
#                                                                              #
################################################################################





#------------------------------------------------------------------------------#
# import required python modules here                                          #
#------------------------------------------------------------------------------#
import os
import sys
import numpy as np
from enum import Enum
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# enum class which distinguishes different recommender systems
#------------------------------------------------------------------------------#
class RSKind(Enum):
  svd = 1  # svd decomposition
  pcc = 2  # pearson correlation
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# get user id from standard input console by asking the user to enter it       #
#------------------------------------------------------------------------------#
def get_user_id(user_count):

  # clear the standard out screen
  os.system("clear")

  # ask user to enter the user id to whom books need to be recommended
  print ("Please enter the user-id to whom books need to be recommended.")
  print ("The valid range for user-id: [1," + str(user_count) + "]")
  print("\n")
  user_id = int(input())

  if user_id < 1 or user_id > user_count:
    print("\nError: user id must be in the range " + "[1," +  \
          str(user_count) + "]." + " exiting gracefully.\n")
    sys.exit()

  return user_id
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# construct an user-movie 2d-matrix where an entry (i,j) holds the rating of   #
# a movie j by user i.                                                         #
#------------------------------------------------------------------------------#
def construct_user_movie_matrix(user_data_base, movie_data_base, \
                                rating_data_base):

   # compute total number of rows.
   n_rows = int(len(user_data_base))

   # compute total number of columns.
   n_cols = int(len(movie_data_base))

   # create matrix object.
   um_mat = np.zeros((n_rows, n_cols))

   # insert user ratings to um_matrix 
   for line in rating_data_base:
     u = int(line[0])
     m = int(line[1])
     r = int(line[2])
     um_mat[u-1, m-1] = r  # since matrix starts from 0th insex, user i stored
                           # in (i-1)th row, and movie j is stored in (j-1)th
                           # col

   # return matrix with its size.
   return n_rows, n_cols, um_mat
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# ask user which recommender system he wants to use                            #
#------------------------------------------------------------------------------#
def get_choice_for_recommender_system():

  os.system("clear")

  print("\n")
  print("enter the choice for recommender systems. following choices are " + \
         "available.")
  print("\n")
  print("----------------------------------------------------------------")
  print("*  enter 1 for svd decomposition based recommender system")
  print("*  enter 2 for pearson correlation based recommender system")
  print("----------------------------------------------------------------")
  print("\n")

  choice = int(input())

  if choice == 1:
    return RSKind.svd
  elif choice == 2:
    return RSKind.pcc
  else:
    print("\n\n")
    print(choice, "is invalid entry for the choice of recommender system." + \
          " exiting gracefully.")
    sys.exit()
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# output top n recommended movies to user                                      #
#------------------------------------------------------------------------------#
def print_recommended_movies(user_id, recommended_list, movie_data_base):

  # clear the standard out screen
  os.system("clear")

  if len(recommended_list) == 0:
    print("\nNo movies to recommend for user_id:", user_id)
  else:
    print("\nFollowing movies are recommended for user_id:", user_id, "\n")
    for m in recommended_list:
      print(movie_data_base[m])
      print("\n")
  print("\n")
#------------------------------------------------------------------------------#
