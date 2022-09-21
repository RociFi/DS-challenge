"""
Interface you must implement on top of your model
"""


import pandas as pd

###Feel free to add additional imports here if necessary

########################################################

class MyModel():
    def __init__(self, PATH_TO_MODEL : str, PATH_TO_DATABASE : str) -> None:
        super().__init__()

        #### Provide code to load your model and your database here
        self._pipeline = None
        self._fraudDB = None
        ###########################################################


    def addressInFraudDB(self, address : str) -> bool:
        """
        Checks to see if an address is contained in the model's fraud db

        Args:
            address (str): the address to check for as a string

        Returns:
            bool: True if it is contained in the db, else false.
        """
        

        ### Provide implementation




        ##########################

        return False


    def fetchFeatures(self, address : str) -> pd.Series:
        """
        If the address is in the DB returns a pandas series containing the data for this address, otherwise 
        returns an empty pandas series.

        Args: 
            address (str): address to check for in DB as string

        Returns:
            pd.Series : pandas series of feature values for the address. Features names on the index, feature values on the values
        """
        
        if self.addressInFraudDB(address):
            ### Provide implementation


            ##########################

            pass
        else:
            return pd.Series(dtype=float)

    def getProbFraud(self, address : str) -> float:
        """ Returns the probability that an address is fraud 

        Args:
            address (str): address as string

        Returns:
            float: probability that address is fraud
        """

        ### Provide implementation


        ##########################

        return 0

    def getScore(self, address : str) -> int:
        """
        Returns a integer score to represent how risky a borrower address is in terms of fraud.

        Args:
            address (str): address as string

        Returns:
            int: Score to denote fraud risk
        """

        ### Provide implementation
        #Note, we leave the scoring implementation up to you. Perhaps you go 0-1000, or 1-10
        #regardless be sure to provide explanation in your docs.

        ##########################

        return 0

    def getPipeline(self):
        return self._pipeline
    def getFraudDB(self):
        return self._fraudDB

    def setPipeline(self, pipeline):
        self._pipeline = pipeline
    def setFraudDB(self, fraudDB):
        self._fraudDB = fraudDB


if __name__ == '__main__':
    
    ### Provide some test code for you interace here ########################

    #you should provide a few test cases to show it was implemented correctly

    #########################################################################
    pass