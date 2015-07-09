################################################################################
#                                                                              #
#                          File Handling Module:                               #
#                                                                              #
################################################################################
#                                                                              #
#   This module implements the different file handling functions               #
#                                                                              #
################################################################################




#------------------------------------------------------------------------------#
# import required python modules here                                          #
#------------------------------------------------------------------------------#
import csv
import sys


#------------------------------------------------------------------------------#
# open data base files                                                         #
#------------------------------------------------------------------------------#
def open_data_base_files():

  # open user data base file
  try:
    user_file = open("./movie_data_set/ml-100k/u.user", 'r', \
                                                          encoding="ISO-8859-1")
  except IOError:
    print("\nError: The user data base file 'u.user' does not exist, exiting " +
          "gracefully.\n")
    sys.exit()

  # open movie data base file
  try:
    movie_file = open("./movie_data_set/ml-100k/u.item", 'r',  \
                                                          encoding="ISO-8859-1")
  except IOError:
    print("\nError: The movie data base file 'u.item' does not exist, exiting "
          + "gracefully.\n")
    sys.exit()

  # open rating data base file
  try:
    rating_file = open("./movie_data_set/ml-100k/u.data", 'r', \
                                                          encoding="ISO-8859-1")
  except IOError:
    print("\nError: The rating data base file 'u.data' does not exist, exiting "
           + "gracefully.\n")
    sys.exit()

  return user_file, movie_file, rating_file
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# close data base files                                                        #
#------------------------------------------------------------------------------#
def close_data_base_files(user_file, movie_file, rating_file):

  user_file.close()
  movie_file.close()
  rating_file.close()
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# read data base files                                                         #
#------------------------------------------------------------------------------#
def read_data_base_files(user_file, movie_file, rating_file):

  # read user data base file
  try:
    user_data_base = list(csv.reader(user_file, delimiter='|'))
  except csv.Error:
    print("\nError: in reading user data base file, exiting gracefully.\n")
    sys.exit()

  # read movie data base file
  try:
    movie_data_base = list(csv.reader(movie_file, delimiter='|'))
  except csv.Error:
    print("\nError: in reading movie data base file, exiting gracefully.\n")
    sys.exit()

  # read rating data base file
  try:
    rating_data_base = list(csv.reader(rating_file, delimiter='\t'))
  except csv.Error:
    print("\nError: in reading rating data base file, exiting gracefully.\n")
    sys.exit()

  return user_data_base, movie_data_base, rating_data_base
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# open train data file and test data file for evaluating the recommender       #
# system                                                                       #
#------------------------------------------------------------------------------#
def open_data_set_files(base, test):

  # include the path
  path = "./movie_data_set/ml-100k/"
  base = path + base
  test = path + test

  # open training set file
  try:
    base_file = open(base, 'r', encoding="ISO-8859-1")
  except IOError:
    print("\nError: The training set file " + "'" + base + "'" +  \
          " does not exist," + " exiting gracefully.\n")
    sys.exit()

  # open test file
  try:
    test_file = open(test, 'r', encoding="ISO-8859-1")
  except IOError:
    print("\nError: The test file " + "'" + test + "'" + " does not exist,"  \
          + " exiting gracefully.\n")
    sys.exit()

  return base_file, test_file
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# read training set and test file                                              #
#------------------------------------------------------------------------------#
def read_training_and_test_files(base_file, test_file):

  # read training set file
  try:
    training_data_base = list(csv.reader(base_file, delimiter='\t'))
  except csv.Error:
    print("\nError: in reading training set file, exiting gracefully.\n")
    sys.exit()

  # read movie data base file
  try:
    test_data_base = list(csv.reader(test_file, delimiter='\t'))
  except csv.Error:
    print("\nError: in reading test file, exiting gracefully.\n")
    sys.exit()

  return training_data_base, test_data_base
#------------------------------------------------------------------------------#
