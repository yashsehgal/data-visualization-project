'''
  This code module is to fetch the data in such a format which can be used
  for data analysis and visualization methods.
  
  fetch_data.py is the module which every module will use to get some amount of dataset and values.
'''

# TODO: To initialize a useful setup for data warehousing.
# TODO: To fetch data from the CSV file and store each type in different containers.
# TODO: To make getters for various features and modules

# ? Check all the features from the CSV files
# ? Manage all the methods and review every feature after performance testing.
# ? Optimise all the features and methods throughout the time of development.

# ! Python Package is not available rightnow
# ! CMakeFile.cmake is currently not generated for this project.

import pandas as pandas


'''
  Creating a class method to manage all the methods
  and features of the codebase module. This class contains all the methods
  and functions for data featching and using.
'''

class FetchData:
  def __init__(self, data_type):
    self.data_type = data_type
    self.check_datafile_type()

  def check_datafile_type(self):
    datatype = self.data_type
    # continue from the datatype method
  
  def fetch_data_from_file(self):
    # opening the csv file to fetch data
    datafile = pandas.read_csv("datasets/dataset.csv")
    
    