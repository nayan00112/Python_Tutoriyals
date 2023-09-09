# Insert the correct syntax for loading JSON files into a DataFrame.

import pandas as pd

a = pd.read_json(r"E:\pythonTutoriyals\Libraries\files\jsn_file.json")

print(a)
#                        day1               day2  ...          day5               day6
# morning        Good morning  Good good morning  ...  Good morning  Good good morning
# evening        Good evening  Good good evening  ...  Good evening  Good good evening
# night                   NaN    good Good night  ...           NaN    good Good night
# early_mornong           NaN                NaN  ...           NaN                NaN

# [4 rows x 6 columns]

