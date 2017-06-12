# HUMAN SORTING

Python function to sort a list of strings in a human-friendly way.

## How to use?


### Clone the project

```
git clone https://github.com/sahilthapar/human-sorting.git  
```
  
### Install dependencies

```
easy_install python-dateutil
pip install flask
```

### Start the server

```
cd human-sorting
export FLASK_APP=server.py
flask run
```

## Sending requests

### Root URL

`http://127.0.0.1:5000`

### URL

`/sort`

### Method

`POST`

### Data parameters

```
    {
        "strings": ["a", "c", "b"]
    }
```

### Success response

```
Code: 200
Content: 
    {
        "sorted_strings": ["a", "b", "c"]
    }
```

## What can be sorted?

1. Numbers
2. Letters
3. Dates (Y-M-D, Y/M/D, D/M/Y, D-M-Y, M-D-Y, M/D/Y, Y/D/M, Y-M-D)
4. Money ($)
5. Phone numbers (123-456-7890)
6. IP Address
7. Scientific notations
8. File paths
9. Versions
10. Alphanumeric
11. Filepaths with numbers, dates

## What can't be sorted?

1. Hexadecimal numbers
2. Date time strings
3. Date strings with formats other than the one mentioned in the list above
4. Days of the week
5. Months of the year
6. Different phone number formats
7. Multi-digit branch numbers in version
8. Different locales
9. Different currencies