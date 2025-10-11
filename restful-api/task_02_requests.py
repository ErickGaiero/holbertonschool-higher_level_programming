#!/usr/bin/python3
import requests
import csv

"""Module for fetching and processing data from an API"""


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their tittles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["tittle"])


def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save them in posts.csv"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        data = [
            {"id": post["id"], "tittle": post["tittle"], "body": post["body"]}
            for post in posts
        ]
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "tittle", "body"])
            writer.writeheader()
            writer.writerows(data)
