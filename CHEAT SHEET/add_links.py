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
            "kronenfeld", "CHEAT SHEET", "cheatsheet.html")
        print("...opening file")
        # Perform operations on the file
        with open(file_path) as f:
            lines = f.readlines()
        print("...reading headings")
        headings=[]
        for line in lines:
            if 'h1 id="' in line:
                headings.append(line)
        print(f"{len(headings)} headings found.")
        topics=[]
        html_links=[]
        for head in headings:
            # patterns:
            # <h1 id="user.letter">user.letter</h1><div class="context">
            # </div><h1 id="c-user-community-lang-c">c :: user / community / lang / c</h1><div class="context">
            head_pieces=head.split('"')
            if len(head_pieces)>1:
                head_link=head_pieces[1]
                keepthis=True
                #filter out repetitive titles
                if head_link[-4:] == 'open':
                    keepthis=False
                if keepthis:
                    short_topic = head_link
                    if len(short_topic) > 0:
                        topics.append(short_topic)
                        html_links.append(f'<button HREF="#{head_link}">{short_topic} </button>')

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
        replace_text = f'<body>\n<div class="link_container"><div class="links">{link_html}</div></div>\n<div class="command_container"><div class="commands">'
        data = data.replace(search_text, replace_text)
        
        # Finish div for commands
        search_text = '</body>'
        replace_text = f'\n</div></div></div></body>'
        data = data.replace(search_text, replace_text)

        # Create div for all contexts
        search_text = '<h1'
        replace_text = '</div><h1'
        data = data.replace(search_text, replace_text)
        data = data.replace(replace_text,'<h1',1)

        search_text = '/h2>'
        replace_text = '/h2><div class="context">'
        data = data.replace(search_text, replace_text)




        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(data)
        
ctx = Context()