'''
  This modules has data visualization methods to analyse the placements on the
  basis of gender. 
  This module is linked with the support module from python-codebase/fetch_data.py
  This module is part of the Development process of this project.
'''

'''
  # TODO: To fetch the genders and placement index from the fetching module
  # TODO: To generate graphs according to the dataset 
  # ? To manage all the methods and functions for graphs and value handlers
'''

from python_codebase.fetch_data import FetchData 

class GenderWisePlacementAnalysis:
  def __init__(self, activation = False):
    self.activation = activation
    
  def generateGraph(self):
     fetchDataObject = FetchData(True)
     print(fetchDataObject.get_gender_list())
  
if __name__ == "__main__":
    genderWisePlacementAnalysis = GenderWisePlacementAnalysis(True)
    genderWisePlacementAnalysis.generateGraph()