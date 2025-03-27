from urllib.request import urlopen

result = urlopen("http://google.com")

print(result.read(1000).decode("utf-8"))