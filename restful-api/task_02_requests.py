#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f'Status Code: {response.status_code}')
    
    if response.status_code == 200:
        posts = response.json()
        for post in postS:
            print(post['title'])

