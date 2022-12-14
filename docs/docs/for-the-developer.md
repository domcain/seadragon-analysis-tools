## Running the code in the development environment
1. **Clone the repository** to your personal computer by running: 
    ```
    $   git clone https://github.com/domcain/seadragon-analysis-tools.git
    ``` 
    in your terminal. 
2. In your terminal, **navigate to/open the cloned repository**.
3. From the seadragon-analysis-tools/ directory, **install the required dependencies** to run the application locally.
    - You can do this using the command: 
        - MacOS: 
        ```
        pip install -r requirements.txt
        ```
        - Windows: 
        ```
        py -m pip install -r requirements.txt
        ```
4. From the `/src` directory, run: 
    ```
    python3 'SDS Analytics.py'
    ```
## Project Layout
```
seadragon-analysis-tools/    
    docs/
        mkdocs.yml                  # The documentation pages configuration file.
        requirements.txt            # Dependencies required to run the documentation locally.
        docs/
            index.md                # The documentation homepage.
            for-the-developer.md    # Documentation relevent to code maintainers.
            user-manual.md          # Documentation relevent to users of the application.
            packages-used.md        # 
            images/
                seadragon.png       # Icon in top left of documentation page.
    src/
        SDS Analytics.py            # Main UI code.
        data_analysis.py            # Code for producing output files.
        images/
           cloud.png                # Image used in the UI.
           sdstitle.png             # Image used in the UI.
           seahorse.gif             # Special image for MacOS Dock icon.
    Test_case/
        Test_cases.csv              # 
        test_data_analysis.py       # Code for testing the output file.
        1/
            inat1.csv               # Test 1.
        2/
            inat2.csv               # Test 2.
        3/
            inat3.csv               # Test 3.
        4/
            inat4.csv               # Test 4.
        5/
            inat5.csv               # Test 5.
        6/
            inat6.csv               # Test 6.
        7/
            inat7.csv               # Test 7.
        8/
            inat8.csv               # Test 8.
        9/
            inat9.csv               # Test 9.
        10/
            inat10.csv              # Test 10.
        11/
            inat11.csv              # Test 11.
        12/
            inat12.csv              # Test 12.
        13/
            inat13.csv              # Test 13.
        14/
            inat14.csv              # Test 14.
    .gitignore                      # File to minimise unnessesary repository file contributions.
    hook-tkinterdnd2.py             # Hook file required to build a python application that uses tkinterdnd2.
    LICENSE.txt                     # License (Creative Commons).
    README.md                       # Initial documentation.
    requirements.txt                # Dependencies required to run the application locally.
```

## SDS Analytics.py

`SDS Analytics.py` acts as the `main.py` seen in a variety of other projects. This file creates the user interface and is responsible for all its functionality.

## data_analysis.py

`data_analysis.py` handles all under the hood operations to produce an Excel workbook from input filepaths, by comparing the contents of the input files.

The only function in `data_analysis.py` that should be called from another file is called analyse_data_files. This function takes two arguments: the first is the filepath of a Seadragon Search file (string), and the second is a list of the filepaths of iNaturalist files (a list of strings). If the function encounters an error, it returns a list of the form \[False, error_message\] (where error_message is a string). If the function executes successfully, it returns a list of the form \[True, preview, suggested_filename, new_wb\] (where preview is a string, suggested_filename is a string, and new_wb is a Workbook, which is a type from the module xlwt).
