import requests
import json

class Parser:
    def __init__(self, username):
        self.username = username
        self.api = 'https://api.github.com/'

    def write_json(self, response):
        with open('data.json', 'w') as wf:
            json.dump(response, wf, indent=2, ensure_ascii=False)
    
    def get_repos(self):
        method = f'users/{self.username}/repos'
        response = requests.get(self.api + method).json()
        self.write_json(response)
        return response

    def parse_repos(self):
        for repo in self.get_repos():
            yield {
                'title': repo['name'],
                'link': repo['html_url'],
                'description': repo['description'],
                'language': repo['language'],
            }


