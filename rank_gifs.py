import requests

API_KEY = 'GwDRiOUvtxTLWkqZXc7ADLTtF41UiXGf'  # Replace with your Giphy API key
BASE_URL = 'https://api.giphy.com/v1/gifs/search'

def fetch_gifs(query):
    try:
        response = requests.get(BASE_URL, params={
            'api_key': API_KEY,
            'q': query,
            'limit': 10,
            'offset': 0,
            'rating': 'g',
            'lang': 'en'
        })
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.RequestException as e:
        print(f"Error fetching GIFs: {e}")
        return []

def rank_gifs(gifs):
    # Simple ranking logic based on the number of views (if available)
    return sorted(gifs, key=lambda x: x.get('images', {}).get('downsized', {}).get('size', 0), reverse=True)

def main():
    query = 'funny'  # Replace with your search term
    gifs = fetch_gifs(query)
    ranked_gifs = rank_gifs(gifs)

    print('Ranked GIFs:')
    for gif in ranked_gifs:
        print(gif.get('url'))

if __name__ == "__main__":
    main()
