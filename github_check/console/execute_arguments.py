import re

regex = re.compile(
        r'^(?:https)?://' # http:// or https://
        r'(?:www.)?' # optional port
        r'github.com' #localhost...
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

print(re.match(regex, "http://www.example.com/local/name") is not None)   # True
print(re.match(regex, "http://www.github.com/local/name") is not None)              # False
print(re.match(regex, "https://www.github.com/local/name") is not None)              # False
print(re.match(regex, "https://github.com/local/name") is not None)              # False