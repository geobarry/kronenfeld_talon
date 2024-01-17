activate jupiter [notebook] [tag]:
	user.activate("jupyter_notebook")
	user.activate("python")
deactivate jupiter [notebook] [tag]:
	user.deactivate("jupyter_notebook")
	user.deactivate("python")
activate fast spots:
	user.activate("fast_spots")
deactivate fast spots:
	user.deactivate("fast_spots")