#precise control over repeat interval	
<user.key> <number> second repeat:
	user.start_repeating("{key}",number*1000)
<user.key> <number> (tic|take) repeat:
	user.start_repeating("{key}",number*100)

#short cut for common intervals
<user.key> slow:
	user.start_repeating("{key}",2500)
<user.key> steady:
	user.start_repeating("{key}",1500)
<user.key> quick:
	users.start_repeating("{key}",500)
<user.key> fast:	
	user.start_repeating("{key}",350)
<user.key> faster:
	user.start_repeating("{key}",200)
<user.key> lightning:	
	user.start_repeating("{key}",100)
