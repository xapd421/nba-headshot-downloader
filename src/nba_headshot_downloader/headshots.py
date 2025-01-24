import requests

def getHeadshotById(id, target_directory=''):
    response = requests.get(f'https://cdn.nba.com/headshots/nba/latest/1040x760/{id}.png', stream=True)

    if not response.ok:
        raise RuntimeError(f"HTTP Request Failed: Status code {response.status_code}")
    
    path = f'{target_directory}/{id}.png' if target_directory else f'{id}.png'

    with open(path, 'wb') as fh:
        for chunk in response.iter_content():
            fh.write(chunk)