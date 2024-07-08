from youtube_search import YoutubeSearch

terms = "cats"  # Your search query
results = YoutubeSearch(terms).to_dict()

for result in results:
    print(f"Title: {result['title']}")
    print(f"Link: {result['link']}")
    print("-"*20)
