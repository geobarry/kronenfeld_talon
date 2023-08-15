#precise control over repeat interval	
<user.key> <number> second repeat:
	user.start_repeating("{key}",number*1000)
<user.key> <number> (tic|take) repeat:
	user.start_repeating("{key}",number*100)

#we shouldn't need this here but the context doesn't seem to be working
stop [repeating]:
	user.stop_repeating()


#short cut for common intervals
<user.key> slow repeat:
	user.start_repeating("{key}",2500)
<user.key> fast repeat:	
	user.start_repeating("{key}",500)

#shortcuts for common keys	
taber:
	user.start_repeating("tab",1000)
(six sir)|sixer:
	user.start_repeating("tab",1000)
laughter|leper:
	user.start_repeating('left',1000)
writer:
	user.start_repeating('right',1000)
(pager down)|(page downer):
	user.start_repeating("pagedown",2000)
(pager up)|(page upper):
	user.start_repeating("pageup",2000)

#these may conflict with other programs such as rango	
upper:
	user.start_repeating("up",1000)
downer:
	user.start_repeating('down',1000)
