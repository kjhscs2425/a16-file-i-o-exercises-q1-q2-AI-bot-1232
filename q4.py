import os
import json
import random 

# Check if the file "data.json" exists.
if os.path.isfile("data.json"):
    # If it does, read "data.json" into the variable `data`
    with open("data.json", "r") as file:
        data = json.load(file)
else:
    # If it doesn't, make an empty dictionary called data
    data = {}

# Get a new recommendation for a new user
name = input("What is your name? ")
recommendation = input("What book/movie/podcast/etc. would you recommend? ")

# Add the new user and recommendation to the `data` dictionary
data[name] = recommendation

# Write the `data` variable to the file "data.json"
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)



random 
[
"i appreciate the reccomandatiom",
"thanks for the recomandation",
]