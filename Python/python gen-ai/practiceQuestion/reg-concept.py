import re

# Pattern match karo
re.match(r"\d+", "123abc")     # start se match
re.search(r"\d+", "abc123")    # kahin bhi dhundo
re.findall(r"\d+", "a1b2c3")   # sab matches list mein
re.sub(r"\d+", "#", "a1b2")    # replace karo

# Common patterns:
# \d  → digit
# \w  → word character
# \s  → whitespace
# .   → koi bhi character
# +   → 1 ya zyada
# *   → 0 ya zyada
# ^   → start
# $   → end

# reg-concept.py
