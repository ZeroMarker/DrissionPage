import requests

def query_whatslink_api(url):
    # API endpoint
    api_url = 'https://whatslink.info/api/v1/link'

    # Parameters
    params = {'url': url}

    try:
        # Make GET request to the API
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

        # Parse JSON response
        data = response.json()

        # Print or process the response data
        print('Content Type:', data['type'])
        print('File Type:', data['file_type'])
        print('Name:', data['name'])
        print('Size:', data['size'])
        print('Count:', data['count'])
        print('Screenshots:', data['screenshots'])

    except requests.exceptions.RequestException as e:
        print('Error:', e)


# Example usage
url_to_query = 'magnet:?xt=urn:btih:EFBD199A54029C15B78B9B11377914603D895955'
query_whatslink_api(url_to_query)
