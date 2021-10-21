#!/usr/bin/env python3

import requests
import json
from faker import Faker


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")


def idx_books():
    r = requests.get(f'{APIHOST}/api/v1/books')
    if r.status_code == 200:
        data_set = r.json()
    else:
        raise Exception(f'Status code {r.status_code} and text {r.text}, while trying to Auth.')
    ls = []
    for i in range(len(data_set)):
        tem = list(data_set[i].values())
        ls.append(tem[0])
    return ls

def deleteBook(bookId, apiKey):
    r = requests.delete(
        f'{APIHOST}/api/v1/books/{bookId}',
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
        }
    )
    if r.status_code == 200:
        print(f'Book {bookId} deleted.')
    else:
        raise Exception(f'Status code {r.status_code} and text {r.text}, while trying to delete Book.')


# Get the Auth Token Key
apiKey = getAuthToken()

# Get the list of IDs of entire library
index_of_books = idx_books()

# Delete the first 5 and the last 5 books
for i in range(5):
    deleteBook(index_of_books[i], apiKey)
    deleteBook(index_of_books[- 1 - i], apiKey)
    