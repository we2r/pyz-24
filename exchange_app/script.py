import requests

updated_post = {
    'title': 'updated title',
    'body': 'updated body',
    'userId': 1
}
post_id = 1
response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=updated_post)
if response.status_code == 200:
    post = response.json()
    print(f"Post updated: ID: {post['id']}, Title: {post['title']}, Body: {post['body']}")
else:
    print(f'Failed to update post with ID {post_id}')