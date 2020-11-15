import sys
import pandas as pd

json_file = sys.argv[1]
csv_name = sys.argv[2]

if type(json_file) is not str:
    json_file = str(json_file)

if type(csv_name) is not str:
    csv_name = str(csv_name)

def json_to_csv(json_file,csv_name = None):
    """Function to convert json file to csv file
    
    Parameters:
    json_file(str): This is the file name of the json file you want to convert.It should include the file extension(.json)
    csv_name(str): This is the name of the output csv file
    
    Returns:
    A converted csv file in the current directory

    """
    data_df = pd.read_json(json_file,lines = True)
    if csv_name == None:
        csv_name = 'converted_file'
    
    return data_df.to_csv(f'{csv_name}.csv')
try:
    
    json_to_csv(json_file,csv_name)
    
except ValueError:
    print("Check if the file name is correct or the file exists in the current folder")