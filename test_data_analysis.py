import unittest
import pandas as pd
import os
from data_analysis import *
import traceback


class TestDataAnalysis(unittest.TestCase):
    def test_data_analysis(self):
        # Read the file that contains all test cases
        df = pd.read_csv('Test_cases.csv')
        input = df["Input"].str.split()
        expected_output = df["Expected Output"]
        description = df["Test Case Description"]
        cwd = os.getcwd()

        # Loop through and test all test cases
        for i in range(input.size):
            os.chdir("./Test_case/"+str(i+1))
            with self.subTest(id=i+1): 
                inat = [];
                for j in range(1,len(input[i])):
                    inat.append(input[i][j])
                try:
                    result = analyse_data_files(input[i][0],inat)
                    try:
                        self.assertEqual(result[1],expected_output[i])
                        print("PASS (id=" + str(i+1) + ")\t: " + description[i]+"\n")
                    except:
                        print("FAIL (id=" + str(i+1) + ")\t: "+ description[i])
                        print("The expected output is '" +expected_output[i] +"', but the actual output is '" + result[1] + "'\n")
                        #print("\n")
                except Exception as e:
                    print("ERROR (id=" + str(i+1) + ")\t: "+ description[i])
                    print(e)
                    print(traceback.format_exc())
                    print("\n")
                

            os.chdir(cwd)
        

        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    