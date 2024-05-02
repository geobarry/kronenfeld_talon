app.exe: msedge.exe
and   win.title: /.*pdf.*/
-
go to page <number>: 
	key(ctrl-alt-g)
	insert("{number}")
	key(enter)
toggle contents: user.pdf_button("Contents")
close read aloud: user.pdf_button("Close read aloud")
zoom width: key(ctrl-\)
rotate: key(ctrl-])
