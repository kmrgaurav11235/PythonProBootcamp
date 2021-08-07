import pandas

valar_scores = {
    "valar": ["Manwe", "Varda", "Ulmo", "Aule", "Yavanna", "Orome", "Vana"],
    "scores": [82, 88, 64, 90, 2, 88, 26]
}

valar_data_frame = pandas.DataFrame(data=valar_scores)

# Looping through a data frame is very similar to looping through a dictionary
# for (valar, score) in valar_data_frame.items():
#     print(valar)
#     print(score)

# The above loop iterates through columns and is not very useful
# If we want to iterate through rows, we use this:
for (index, row) in valar_data_frame.iterrows():
    # Each of the 'row' is a panda Series object
    print(f"{index + 1}. {row.valar}\t{row.scores}")
