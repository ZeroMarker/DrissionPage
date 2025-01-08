"""
NVDA
"LL"
(XX)
-000
(#some)
(from:Apple)
(to:X)
(@elonmusk)
min_replies:100
min_faves:100
min_retweets:100
lang:ko
until:2023-06-10
since:2014-02-04
filter:links
filter:replies
"""

# https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators
base = "https://twitter.com/search"

"exact"

since:2024-12-31

until:2024-12-31

from:@elonmusk

lang:en 

filter:videos

-filter:media

near:"New York" within:10mi

