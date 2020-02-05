import re
link = 'https://i.redd.it/0u87s5o7awe41.jpg'
title = re.compile(r'/\w+(?:\.\w{3}$)')
parsed = title.findall(link)
#convert list to string so its only single element
parsed = parsed[0]
final = ''
for i in range(1,len(parsed)):
    if parsed[i] == '.':
        break
    else:
        final += parsed[i]