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
    self.serial_number = datafile[datafile.sl_no]
    self.gender_list = datafile[datafile.gender]
    self.number_of_males = len(datafile[datafile.gender == 'M'])
    self.number_of_females = len(datafile[datafile.gender == 'F'])
    self.secondary_school_percentage = datafile[datafile.ssc_p]
    self.secondary_school_board = datafile[datafile.ssc_b]
    self.number_of_central_board_secondary = len(datafile[datafile.ssc_b == "Central"])
    self.number_of_other_board_secondary = len(datafile[datafile.ssc_b == "Others"])
    self.high_school_percentage = datafile[datafile.hsc_p]
    self.high_school_board = datafile[datafile.hsc_b]
    self.number_of_central_board_high = len(datafile[datafile.hsc_b == "Central"])
    self.number_of_other_board_high = len(datafile[datafile.hsc_b == "Others"])
    self.high_school_subjects = datafile[datafile.hsc_s]
    self.high_school_arts = len(datafile[datafile.hsc_s == "Arts"])
    self.high_school_science = len(datafile[datafile.hsc_s == "Science"])
    self.high_school_commerce = len(datafile[datafile.hsc_s == "Commerce"])
    self.college_degree = datafile[datafile.degree_t]
    self.number_of_commerce_management_degree = len(datafile[datafile.degree_t == "Comm&Mgmt"])
    self.number_of_science_tech_degree = len(datafile[datafile.degree_t == "Sci&Tech"])
    self.number_of_other_degree = len(datafile[datafile.degree_t == "Others"])
    self.college_marks = datafile[datafile.degree_p]
    self.work_experience = datafile[datafile.workexp]
    self.number_of_no_workexp = len(datafile[datafile.workexp == "No"])
    self.number_of_yes_workexp = len(datafile[datafile.workexp == "Yes"])
    self.emp_test_percentage = datafile[datafile.etest_p]
    self.students_specialization = datafile[datafile.specialisation]
    self.number_of_mkt_hr_spec = len(datafile[datafile.specialisation == "Mkt&HR"])
    self.number_of_mkt_fin_spec = len(datafile[datafile.specialisation == "Mkt&Fin"])
    self.mba_percentage = datafile[datafile.mba_p]
    self.student_placement_status = datafile[datafile.status]
    self.number_of_student_placed = len(datafile[datafile.status == "Placed"])
    self.number_of_student_not_placed = len(datafile[datafile.status == "Not Placed"])
    self.salary_index = datafile[datafile.salary]
    
    