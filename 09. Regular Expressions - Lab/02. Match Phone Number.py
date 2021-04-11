# \+359\s2\s\d{3}\s\d{4}|\+359-2-\d{3}-\d{4}\b

import re
numbers = input()
regex = r"\+359\s2\s\d{3}\s\d{4}|\+359-2-\d{3}-\d{4}\b"
matches = re.findall(regex, numbers)
print(", ".join(matches))