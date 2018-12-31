# getting data from the ACLU Torture Database api
# This python script will grab the data from each "node" in the ACLU's online database

# first step is importing the python packages/modules you need

import requests
import json
import time

# next stage -- run through the website nodes and get what you need
# this is a while loop based on node number (each doc/entity has a node number on the site based on the drupal platlform used to host it)
# all entities used by ACLU database have node numbers (documents, officials, incidents, techniques, etc)
# many were uploaded to the system in sets, so large groups by type exist in sequential node nums
# the bulk of the Document node types, for example, are between 
#   node ID == 2289  and node ID == 7277
# but best to grab data from all nodes -- but do it in chunks so as to not overload ACLU server all at once
# Run this code below in groups of 1000 during development, beginning w/0 to 1000
# in code below: REPLACE "0" AND "13000" EACH TIME WITH HIGH/LOW OF 1000s
# for example, run the below, replacing "13000" with "1000" so that it only runs for nodes from 0 to 1000, then...
# after that replace "0" with "1000" and replace "1000" with "2000"
# Repeat, increasing by 1000 each time and letting some time pass between each run until at 13,000 current max nodes

node = 13000


while node > 0:
  
  url = ('https://www.thetorturedatabase.org/rest/fullnode/retrieve.json?nid=') + str(node)

  singledoc = requests.get(url)
  singledoc_json = singledoc.json()


  
  # if you want to, you can print to see how this stage is going
  # print(singledoc_json)
  
  data = json.loads(singledoc.text)

  # this continue statement is to keep it from choking on a no-results node ID
  # also adjusts node number down 1 so that next req will move to next item
  if isinstance(data,list)==True: 
  	node = node - 1  
  	continue

  doc_nid = (singledoc_json['nid'])


  print(doc_nid)

  
  # make folder called "aclu_data" in same folder as script to receive results
  # this should create the results and save as JSON in that folder
  json.dump(data,open('aclu_data/aclu_'+str(node)+'.json','w'),indent=2)

  
  node = node - 1 
  time.sleep(1)

    # time so will have a short sleep between each loop




# this script transforms the results into the set of jsons (1 for each node) which can then be queried or worked with as a set

# a separate python script can be used to generate a CSV file from the mutliple JSON results in the next step
