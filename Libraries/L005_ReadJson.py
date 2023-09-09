# Read JSON
# Big data sets are often stored, or extracted as JSON.

# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.


import pandas as pd

a = pd.read_json(r"E:\pythonTutoriyals\Libraries\files\jsn_file.json")

print(a)
#                        day1               day2  ...          day5               day6
# morning        Good morning  Good good morning  ...  Good morning  Good good morning
# evening        Good evening  Good good evening  ...  Good evening  Good good evening
# night                   NaN    good Good night  ...           NaN    good Good night
# early_mornong           NaN                NaN  ...           NaN                NaN

# [4 rows x 6 columns]


# Tip: use to_string() to print the entire DataFrame.
print(a.to_string())
#                        day1               day2                                               day3                                               day4          day5               day6
# morning        Good morning  Good good morning                        [Good, good, good, morning]                        [Good, good, good, morning]  Good morning  Good good morning
# evening        Good evening  Good good evening                        [Good, good, good, evening]                        [Good, good, good, evening]  Good evening  Good good evening
# night                   NaN    good Good night                                    good good night                                    good good night           NaN    good Good night
# early_mornong           NaN                NaN  {'good1': 'Surya namaskar', 'good2': 'Excersics'}  {'good1': 'Surya namaskar', 'good2': 'Excersics'}  




# Dictionary as JSON
# JSON = Python Dictionary

# JSON objects have the same format as Python dictionaries.

# If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:

mydictnary = {
    "apple": "apple is red.",
    "orange": "orange is orange!",
    "guava" : "guava is green",
    "fruits colors": ['red', 'orange', 'green', 'browen', 'yellow']
}
dict_df = pd.DataFrame(mydictnary) 
print(dict_df.to_string())
#            apple             orange           guava fruits colors
# 0  apple is red.  orange is orange!  guava is green           red
# 1  apple is red.  orange is orange!  guava is green        orange
# 2  apple is red.  orange is orange!  guava is green         green
# 3  apple is red.  orange is orange!  guava is green        browen
# 4  apple is red.  orange is orange!  guava is green        yellow
