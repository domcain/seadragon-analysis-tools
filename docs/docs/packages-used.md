# Packages Used

Listed below are the imported python modules used in this project.

??? note "Need more info?" 
    Click on any of the headings to read module documentation.


## User Interface 
`SDS Analytics.py` acts as the `main.py` seen in a variety of other projects. This file creates the user interface.

[tkinter](https://docs.python.org/3/library/tkinter.html) is the standard Python interface to the Tcl/Tk GUI toolkit. This package provides the building blocks of the user interface.

[tkinterdnd2](https://pypi.org/project/tkinterdnd2/): This package provides the 'drag & drop' functionality to the interface. 

## Data Analysis 
`data_analysis.py` handles all under the hood operations taking input file paths, and producing an excel file comparing the contents of the input files.

[xlrd](https://pypi.org/project/xlrd/): This package provides the tools required to read and analyse data from input excel files.

[xlwt](https://pypi.org/project/xlwt/): This package provides the tools to generate the output excel file.

[openpyxl](https://pypi.org/project/openpyxl/): This package provides the tools to read/write excel files other than .xls, such as .xlsx, .xlsm, .xltx, .xltm
