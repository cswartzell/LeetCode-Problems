import re

# startUrl = "http://news.yahoo.com/news/topics/"
startUrl = "fuckingfinally/nopestillballs"

slash_idx = re.search(r"(?<!\/)\/(?!\/)", startUrl)
# slash_idx = re.search(r"/", startUrl)
slash_idx = slash_idx.start() if slash_idx else None
print(slash_idx)
