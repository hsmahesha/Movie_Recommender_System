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
# construct training set and test set 2d-matrix where an entry (i,j) holds the #
# rating of a movie j by user i.                                               #
#------------------------------------------------------------------------------#
def construct_rating_matrix(data_base):

  # compute total number of rows.
  temp_file = sorted(data_base, key=lambda arg: int(arg[0]), reverse=True)
  n_rows = int(temp_file[0][0])

  # compute total number of columns.
  temp_file = sorted(data_base, key=lambda arg: int(arg[1]), reverse=True)
  n_cols = int(temp_file[0][1])

  # create matrix object.
  mat = np.zeros((n_rows, n_cols))

  # insert user ratings to um_matrix 
  for line in data_base:
    u = int(line[0])
    m = int(line[1])
    r = int(line[2])
    mat[u-1, m-1] = r     # since matrix starts from 0th insex, user i stored
                          # in (i-1)th row, and movie j is stored in (j-1)th
                          # col

  # return matrix with its size.
  return n_rows, n_cols, mat
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# construct user-movie rating dictionary                                       #
#------------------------------------------------------------------------------#
def construct_rating_dict(data_base):

  u_dict = {}
  for item in data_base:
    u = int(item[0])
    m = int(item[1])
    r = int(item[2])
    if u in u_dict:
      r_dict = u_dict[u]
    else:
      r_dict = {}
    r_dict[m] = r
    u_dict[u] = r_dict

  return u_dict
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

#------------------------------------------------------------------------------#
# parse command line arguments of emain()                                      #
#------------------------------------------------------------------------------#
def parse_emain_command_line_args(argv):

  if len(argv) != 3:
    print("\n")
    print("Error: invalid number of command line arguments")
    print("Usage: python emain.py train_data_file test_data_file")
    print("\n")
    sys.exit()

  return argv[1], argv[2]
#------------------------------------------------------------------------------#
