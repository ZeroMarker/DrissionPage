import urllib
import HTMLParser

# This is the magnet link to modify
magnetLink = 'magnet:?xt=urn:btih:b54a3ba68fd398ed019e21290beecc9dda64a858&dn=wikipedia_en_all_novid_2018-06.zim&tr=udp%3a%2f%2ftracker.mg64.net'

# Here is a list of trackers to insert into the torrent
trackers = {'list', 'of', 'trackers'}

# Convert HTML special characters to escaped normal characters
magnetLink = urllib.unquote(magnetLink).decode('utf8')
magnetLink = HTMLParser.HTMLParser().unescape(magnetLink)

# Split out the trackers from the magnet link and save for later
magnetsplit = magnetLink.split('&tr=')
base = magnetsplit[0]
magnetTrackers = magnetsplit[1::]

# Add the trackers from the magnet link to our list of trackers
for magnetTracker in magnetTrackers:
    trackers.add(magnetTracker)

# Add the trackers
magnetLink = base
for tracker in trackers:
    magnetLink += '&tr=' + tracker

# Create the torrent file name - it is named after the magnet hash
magnetName = magnetLink[magnetLink.find("btih:") + 1:magnetLink.find("&")]
magnetName = magnetName.replace('tih:', '')
torrentfilename = 'meta-' + magnetName + '.torrent'

# Write the magnet link to the torrent file
with open(torrentfilename, 'w') as o:
    linkstr = u'd10:magnet-uri' + str(len(magnetLink)) + u':' + magnetLink + u'e'
    linkstr = linkstr.encode('utf8')
    o.write(linkstr)