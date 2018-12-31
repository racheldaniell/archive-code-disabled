# Before any next steps, backup the folder of your original ACLU data grabs just in case

# This python script looks through the folder of individual JSON files representing ACLU Torture FOIA Database data
# It loops through them to find only the ones that are from data/node type = "document"
# From those JSON files of document data, it pulls some of the data elements of interest
# It then generates a CSV file from those data elements.
# The resulting CSV file can be used in a multitude of ways!


# First, import some toolsets to use for this process
# json will help python read the JSON files
# glob will help python work with multiple files as a set
# os will help it work with file paths
# csv will let it generate a CSV file from the data

import json
import glob 
import os
import csv


# use the os toolset to call the directory with the files in it; swap with your path

os.chdir("/Users/racheljdaniell/Desktop/py_my_scripts/aclu_pys/aclu_data")

# make a CSV file where we will put the data from the multiple JSON files

csvfile = open('output_doc.csv','w') 
csvwriter=csv.writer(csvfile)

# next we give our CSV file a header row
# note that it is good to doublecheck this header row code with your for loop code and your writerow code to make sure all have matching elements

header = ['rec_id','rec_type','rec_title','doc_date','rel_date','doc_type','doc_descr','doc_handwrit','doc_pdf','doc_text']
csvwriter.writerow(header)

# now for some python magic - looping through all the files in the directory and pulling data

for file in glob.glob("*.json"): #iterates over all files in the directory 

   with open(file) as get_txt:
        
        json_data = json.load(get_txt)

        #if type is a doc then grab the data from relevant fields/dictionaries/lists
        if json_data['type'] == 'document':
            rec_id = json_data['nid']
            rec_type = json_data['type']
            rec_title = json_data['title']
            doc_date = json_data['field_doc_date'][0]['value']
            rel_date = json_data['field_doc_release_date'][0]['value']
            doc_type = json_data['field_doc_type'][0]['value']
            doc_descr = json_data['field_doc_description'][0]['value']
            doc_handwrit = json_data['field_doc_handwritten_text'][0]['value']
            if json_data['field_doc_pdf'][0] == None: 
                doc_pdf = ' '
            else:
                doc_pdf = 'https://www.thetorturedatabase.org/'+json_data['field_doc_pdf'][0]['filepath']
            doc_text = json_data['field_doc_text'][0]['value']

            # print statements just to let us know the loop is able to grab correct data
            # these are optional -- feel free to run the code without these print statements
            print(rec_id)
            print(rec_type)
            print(rec_title)
            print(doc_descr)

            #for each doc record make a row in our CSV
            # it's good to doublecheck that number and order here match our header row above
            row = [rec_id,rec_type,rec_title,doc_date,rel_date,doc_type,doc_descr,doc_handwrit,doc_pdf,doc_text]
            csvwriter.writerow(row)

  # At the end of running this code you'll have a CSV file of ACLU Torture FOIA Database data to work with in any way you want to!
  # This ultimately adds to the "circulate-ability" of this government information -- adding to govt. transparency
  # Maximizing the availability of this information can help to empower people to understand past actions of the US government