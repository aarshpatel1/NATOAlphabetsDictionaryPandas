# working with dictionaries and panda's dataframes with loops
import pandas

# concept code
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # print(key)
    # print(value)
    # print(f"{key} : {value}")
    pass

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows of a data frame
# syntax of Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row.student)
    # print(row["student"])
    # print(row.score)
    # print(row["score"])
    pass
