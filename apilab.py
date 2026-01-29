"""
API LAB: Calling Real Data from the Internet

GOAL:
Learn how to use an API to get real data from the internet using Python.

An API is just a URL that returns DATA instead of a webpage.
"""

# STEP 1: Choose an API (USE THIS LIST ONLY) 

# Pick ONE API from this list on schoology https://github.com/teacher-aj/public-apis?tab=readme-ov-file#social


# STEP 2: Make an API Call

# Paste the API URL you chose as a STRING below

# Convert the response into Python data (dictionary or list) below

# ALWAYS print the full data first so you can see its structure

import requests

url = "https://api.spacexdata.com/v5/launches/latest"

response = requests.get(url)
data = response.json()


# STEP 3: Extract a Piece of Data

# Look at what printed above.
# Find ONE specific value you want to use.

# Examples (yours will be different):

# cat_fact = data["fact"]
# print(cat_fact)

# latitude = data["iss_position"]["latitude"]
# print(latitude)

# write your code here
landing = data["cores"][0]["landing_success"]

if landing == True:
    landing = "Yes"
else:
    landing = "No"

    
print("Did SpaceX demo launch number 94 on May 30, 2020 land successfully?")
print(landing)

# STEP 4: Do Something With the Data


# Do ONE of the following:
# - Print it in a sentence
# - Store it in a variable
# - Add it to a list
# - Combine it with text

# Example:
# print(f"The ISS is currently at latitude {latitude}.")
