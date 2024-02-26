from talon import Context,Module,actions  
mod = Module()

@mod.action_class
class Actions:
    def add_links_to_cheatsheet():
        """Adds links to the top of the cheatsheet created by Tara Roys code"""
        #add links to cheat sheet
        print("ADD LINKS TO CHEATSHEET")
        print("...import os")
        import os
        appdata_path = os.getenv('APPDATA')
        file_path = os.path.join(
            appdata_path, "talon", "user",
            "kronenfeld_talon", "CHEAT SHEET", "cheatsheet.html")
        print("...opening file")
        # Perform operations on the file
        with open(file_path) as f:
            lines = f.readlines()
        print("...reading headings")
        headings=[]
        for line in lines:
            if 'id="' in line:
                headings.append(line)
        print(f"{len(headings)} headings found.")
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

        # Read the file content
        with open(file_path, 'r') as file:
            data = file.read()

        # Add div for link and begin div for commands
        search_text = '<body>'
        replace_text = f'<body>\n<div id="links">{link_html}</div>\n<div id="commands">'
        print(replace_text)
        data = data.replace(search_text, replace_text)
        
        # Finish div for commands
        search_text = '</body>'
        replace_text = f'\n</div></body>'
        data = data.replace(search_text, replace_text)

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(data)
        
ctx = Context()