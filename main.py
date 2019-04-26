import requests, sys,os
from dotenv import load_dotenv

load_dotenv()

def search_movie(*args):
    movie_name = " ".join(args)
    apikey = os.getenv('apikey')
    url = f"http://omdbapi.com/?apikey={apikey}&t={movie_name}"

    result = requests.get(url)

    if result.status_code == 200:
        return result.json()
    else:
        print("Request gelmedi")
        exit()


if len(sys.argv) < 3:
    print("Alinmadi")
    exit()
else:
    if sys.argv[1] == 'movie':
        result = search_movie(*sys.argv[2:])
        if result['Response'] == 'False':
            print(result['Error'])
            exit()
        else:
            print('Title: ', result['Title'])
            print('Year: ', result['Year'])
            print('Released: ', result['Released'])
    