# JSON TO CSV

This script converts a given json file to csv. The headings of the column are the json keys,whole the data in the rows are the json values

-[Prerequisites]#(prerequisites)
-[Usage]#(usage)


##  Prerequisites
This script requires:

- [Pandas]
- [Python3]

Ensure you have python3 installed in your system

Run the below command to install pandas library

''' pip install pandas '''


## Usage

1. Ensure the script is in the same directory(folder) as your json file

The structure of your directory should be

'''
|-- json_to_csv.py
|-- file.json(your json file)

'''

You can now run the script as

''' python json_to_csv.py file.json output_csv_name '''

example:
''' python json_to_csv.py pet.json pet '''

This will output a file 'pet.csv' in the current directory