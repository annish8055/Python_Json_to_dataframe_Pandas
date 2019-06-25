import pandas as pd
import json

with open("./jsonfiles/data2.json") as json_file:  
    file_data = json.load(json_file) 

data = pd.DataFrame.from_dict(file_data,orient='columns')
#f= open("./output/data.csv","w")
#f.write("Ann\n")
#f.close()
data.to_csv ("./output/data.csv", mode='w', index = None, header=True)
