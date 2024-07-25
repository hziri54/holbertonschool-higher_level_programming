import requests
import csv

def fetch_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return response.json() if response.status_code == 200 else None

def print_posts_titles(posts):
    for post in posts:
        print(post['title'])

def save_posts_to_csv(posts, filename='posts.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(posts)

posts = fetch_posts()
if posts:
    print_posts_titles(posts)
    save_posts_to_csv(posts)
