import re

TIME_ISO8601_REGEX = re.compile(r'^\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}Z', re.IGNORECASE)
URL_REGEX = re.compile(r'(?<=<).*?(?=>)', re.IGNORECASE)
REL_REGEX = re.compile(r'(?<=rel=").*?(?=")', re.IGNORECASE)
GITHUB_URL_REGEX = None