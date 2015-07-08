################################################################################
#                                                                              #
#                               Data Module:                                   #
#                                                                              #
################################################################################
#                                                                              #
#   This module implements a class Data which holds all required data          #
#                                                                              #
################################################################################





#------------------------------------------------------------------------------#
# class Data:                                                                  #
#------------------------------------------------------------------------------#
class Data:

  #----------------------------------------------------------------------------#
  # public data members                                                        #
  #----------------------------------------------------------------------------#
  um_mat = None
  n_rows = None
  n_cols = None
  user_id = None
  top_n = None
  knn =  None
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # special init method to initialize an object of type 'Data'                 #
  #----------------------------------------------------------------------------#
  def __init__(self, um_mat, n_rows, n_cols, user_id):

    self.um_mat = um_mat          # user-movie matrix
    self.n_rows = int(n_rows)     # number of users 
    self.n_cols = int(n_cols)     # number of movies
    self.user_id = int(user_id-1) # input user to whom movies to be recommend.
                                  # since matrix index starts with 0th loc, we
                                  # need to take one less than actual user-id
                                  # for computation purpose
    self.top_n = int(10)          # number of movies to be recommend
    self.knn = int(14)            # k nearest neighbor users
  #----------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
