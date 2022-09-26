import unittest
import pandas as pd
from data_analysis import *

class TestDataAnalysis(unittest.TestCase):
    def test_data_analysis(self):
        # Read the file that contains all test cases
        df = pd.read_csv('Test_cases.csv')
        input = df["Input"].str.split()
        expected_output = df["Expected Output"]

        # Loop through and test all test cases
        for i in range(input.size):
            with self.subTest(id=i+1):              
                result = analyse_data_files("./Test_case/"+str(i+1)+"/"+input[i][0],"./Test_case/"+str(i+1)+"/"+input[i][1])
                self.assertEqual(result[1],expected_output[i])
        
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
