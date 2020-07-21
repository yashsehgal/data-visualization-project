'''
  This modules has data visualization methods to analyse the placements on the
  basis of subjects taken in 12th Standard (High School). 
  This module is linked with the support module from python-codebase/fetch_data.py
  This module is part of the Development process of this project.
'''
'''
  # TODO: To fetch the genders and placement index from the fetching module
  # TODO: To generate graphs according to the dataset 
  # ? To manage all the methods and functions for graphs and value handlers
'''

from python_codebase.fetch_data import FetchData as FetchData
from matplotlib import pyplot as plt

class SubjectWisePlacementAnalysis:
  def __init__(self, activation = False):
    self.activation = activation
  
  def generateGraph(self):
    # activation of the fetchData object which will inherit the properties 
    # FetchData class method
    fetchData = FetchData(True)
    
    subject_list = fetchData.get_high_school_objects()
    print(subject_list)
    
    # plt.plot()
  
if __name__ == '__main__':
  fetchData.generateGraph()
  
  