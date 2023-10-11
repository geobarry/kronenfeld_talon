#add links to cheat sheet
file_name=r'%appdata%\talon\user\kronenfeld_talon\CHEAT SHEET\cheatsheet.html'

with open(file_name) as f:
    lines = f.readlines()
headings=[]
for line in lines:
    if 'id="' in line:
        headings.append(line)
print(len(headings))
topics=[]
html_links=[]
for head in headings:
    topicpieces=head.split('"')
    if len(topicpieces)>1:
        topic=topicpieces[1]
        keepthis=True
        #filter out repetitive titles
        if topic[-4:] == 'open':
            keepthis=False
        if len(topics) > 0:
            if topic.split('-')[0] == topics[-1].split('-')[0]:
                keepthis=False
        if keepthis:
            topics.append(topic)
            html_links.append('<a HREF="#{}">{}</a>'.format(topic,topic))

topiclist=topics[0]
link_html=html_links[0]
for t,h in zip(topics[1:],html_links[1:]):
    topiclist=topiclist+'|'+t
    link_html=link_html+'|'+h
print(link_html)
