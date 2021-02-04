


import pandas as pd
names = pd.read_csv("IndianNames.csv")




cleaned_name = []
for name in names['Names']:
    first_name = str(name).strip().split(" ")[0]
    if len(first_name) > 2:
        cleaned_name.append(first_name)
    
unique_names = set(cleaned_name)
unique_names = sorted(list(unique_names))
data = pd.DataFrame(unique_names, columns=['Name'])
data.to_csv('cleaned_indian_names.csv',index=False)






