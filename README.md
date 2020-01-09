
# A Simple API for splitting strings and identify blacklisted strings

## Main
This is build on a Flask-RestPlus framework.
A simple endpoint where you can make a post request with a long string without spaces.
The API will split the string for you and then identify the blacklisted words which is passed
via a file. 

## Installation
```
# Clone the application to your local computer
git clone https://github.com/guohaolee/stringsplitter.git

# Start up the docker
cd stringsplitter
docker-compose up --build -d

# Visit the api page:

http://0.0.0.0:8000/api/v1

You should be able to see a swagger page

# Accessing the endpoints:
You can access via the swagger documentation on the link above,
OR
You can easily passed the string via the url as below using Curl:

curl -X POST "http://localhost:8000/api/v1/stringvalidation/MSSQLhsqldbLovebeersAuthorizationPHPRunningGymmssqlJavaScript" -H "accept: application/json"


The sample returned result will be as below in a json format:

Params:
- message: Update you the status of the API call
- output: The splitted strings from the input
- blaclisted: List of words which is categorized as blacklisted based on the "blacklist_strings.txt" file

{
  "message": "Success",
  "output": "MSSQL hsqldb Love beers Authorization PHP Running Gym mssql JavaScript",
  "blaclisted": [
    "MSSQL",
    "Authorization",
    "PHP",
    "Running",
    "Gym",
    "JavaScript"
  ]
}


# List docker options
docker ps

# Check docker logs
docker logs api_project_api_1

# Enter to the docker container
docker exec -it stringsplitter_api-string_1 bash

# Exit docker container
exit

# Once done, remove the docker container
docker-compose down
```

## Improvising String Split
To further improve on the string split accuracy, we can add our own words to the file "words_library.txt.gz"
This text file is situated in the /dev folder
To add words into it, you'll need to unzip it and then add words into it.
Then rezip it.
The higher the words in the file, the higher the probability.
Library reference: https://github.com/keredson/wordninja

## Blacklisted Words
After splitting the string, the words are stored in a list. Each words in the list will be compared
with blacklisted words from the file "blacklist_strings.txt in the /dev folder.
To add more words into the blacklist, simply adding/removing words in the file.
