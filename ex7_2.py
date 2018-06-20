# Modify 'match = re.findall(r'/product="([^"]+)"', gb, re.DOTALL)'
# for results without 'isoform' in them
# Try to use negative lookahead assertion
import re
gb = open("NC_000072.6.gb").read()
match = re.findall(r'/product="([^"]+)"', gb, re.DOTALL)
match2 = re.findall('/product="(rhodopsin[^"](?!isoform)[^"]+)"', gb, re.DOTALL)
print match, '\n\n\n', match2
