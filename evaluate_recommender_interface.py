################################################################################
#                                                                              #
#                     Movie Recommender System Interface:                      #
#                                                                              #
################################################################################



#------------------------------------------------------------------------------#
# import required built-in python modules here                                 #
#------------------------------------------------------------------------------#
import os
import sys
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# add path to movie recommender package before importing modules from this     #
# package                                                                      #
#------------------------------------------------------------------------------#
sys.path.insert(0, "./package")
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# import modules from movie recommender package here                           #
#------------------------------------------------------------------------------#
import package.file_handler.fh as fh
import package.utility.util as util
import package.data.data as d
import package.recommender as recom
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# import classes and other stuffs from above modules                           #
#------------------------------------------------------------------------------#
from package.utility.util import *
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# main interface function of movie recommender system                          #
#------------------------------------------------------------------------------#
def evaluate_movie_recommender_system(argv):

  # parse command line arguments
  base, test = util.parse_emain_command_line_args(argv)

  # open training set file and test file
  base_file, test_file = fh.open_data_set_files(base, test)

  # read training file and test file
  training_data_base, test_data_base = fh.read_training_and_test_files( \
                                       base_file, test_file)

  # ask user which recommender system he wants to evaluate
  choice = util.get_choice_for_recommender_system()

  # contruct training set 2d-matrix where an entry (i,j) contains the rating
  # of movie j+1 by user i+1. this is because, matrix starts from 0th index.
  n_rows, n_cols, tr_mat = util.construct_rating_matrix(training_data_base)
#------------------------------------------------------------------------------#
