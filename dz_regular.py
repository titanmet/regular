import requests
import re

def get_habrahabr():
    r = requests.get('http://habrahabr.ru')
    print(r.content)
    name_pattern = r'(https?://[\w.-]+)'
    name = re.findall(name_pattern, str(r.content))
    print(name)



if __name__ == '__main__':
    get_habrahabr()

