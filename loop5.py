sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
sample_dict2 = ["name", "salary"]

for key in sample_dict2:
    del sample_dict[key]

print(str(sample_dict))

