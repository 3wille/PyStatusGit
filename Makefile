mkfile_dir:=$(shell pwd)

install:
	ln -s $(mkfile_dir)/git_status.py /usr/lib/python3.7/site-packages/i3pystatus/git_status.py
