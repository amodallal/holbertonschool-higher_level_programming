#!/usr/bin/python3
"""Script to interact with JSONPlaceholder API and process post data."""
import requests
import csv


def fetch_and_print_posts():
    """Fetch and print all post titles from JSONPlaceholder."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save them into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        post_data = [{"id": post["id"], "title": post["title"], "body": post["body"]}
                     for post in posts]

        with open("posts.csv", mode="w", newline='', encoding="utf-8") as csv_file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(post_data)
