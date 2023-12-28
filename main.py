# Victor Flucus Last Edit 19DEC23
# <!-- WIP --!>

# Standard Library Imports 
import os
from pprint import pprint as pp;

#Project Library Imports 
from formula_validator import validating_tools;


#Instantiate class with provided url --TO DO: Get URL from GUI---
workfront_data = validating_tools.StreamClient('https://lonza.my.workfront.com/project/655438a4002709a80b2dd4f915205123/tasks')
#Get dictionary of task from project (json format)
pp(workfront_data.get_project_tasks())

#Get DeltaV Export (XML format) in to JSON format
deltaV_data = validating_tools.XMLtoJSON('C:/Users/dev_vflucus/Documents/Buffer Run/Sandbox/learning_xml/PR-SUM-DSP.xml')
deltaV_data_converted = deltaV_data.convert()

#--DEBUGGING STEP-- write converted data to a text file for review 
current_dir = os.getcwd()
file_path = os.path.join(current_dir, "deltaV_json.txt") 
with open(file_path, "w") as json_file:
        json_file.write(deltaV_data_converted)
