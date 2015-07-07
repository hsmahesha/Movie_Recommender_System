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
import package.movie_data.md as md
import package.recommender as recom
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# main interface function of movie recommender system                          #
#------------------------------------------------------------------------------#
def movie_recommender_system():

  # open all data base files.
  user_file, movie_file, rating_file = fh.open_data_base_files()

  # read data base files.
  user_data_base, movie_data_base, rating_data_base = \
                     fh.read_data_base_files(user_file, movie_file, rating_file)

  # get user-id to whom movies need to be recommended.
  user_id = int(util.get_user_id(len(user_data_base)))

  # contruct an user-movie 2d-matrix where an entry (i,j) contains the rating
  # of movie j+1 by user i+1. this is because, matrix starts from 0th index.
  n_rows, n_cols, um_mat = util.construct_user_movie_matrix( \
                              user_data_base, movie_data_base, rating_data_base)

  # construct a Data object
  data = md.Data(um_mat, n_rows, n_cols, user_id)

  # call public interface method of class Recommender and get the list of 
  # movies to be recommended for user_id
  recommended_list = recom.recommend(data)

  # output top n recommended list of movies 
  util.print_recommended_movies(user_id, recommended_list, movie_data_base)

  # close data base files
  fh.close_data_base_files(user_file, movie_file, rating_file)
#------------------------------------------------------------------------------#
