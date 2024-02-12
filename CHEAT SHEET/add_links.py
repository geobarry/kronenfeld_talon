from talon import Context,Module,actions
mod = Module()

@mod.action_class
class Actions:
    def add_links_to_cheatsheet():
        """Adds links to the top of the cheatsheet created by Tara Roys code"""
        #add links to cheat sheet
        
        import os
        appdata_path = os.getenv('APPDATA')
        file_path = os.path.join(appdata_path, "talon", "user", "kronenfeld_talon", "CHEAT SHEET", "cheatsheet.html")


        # Perform operations on the file
    
        with open(file_path) as f:
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
            topiclist=topiclist+' | '+t
            link_html=link_html+' | '+h
        
        print(link_html)
        # Define the file path and the text to be replaced and its replacement
        search_text = '<body>'
        replace_text = f'<body>\n{link_html}'

        # Read the file content
        with open(file_path, 'r') as file:
            data = file.read()

        # Replace the target text
        data = data.replace(search_text, replace_text)

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(data)

ctx = Context()