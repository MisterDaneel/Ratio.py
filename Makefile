ratio.py:
	echo "Please run : sudo make install"
install:
	install --mode=775 ./ratio.py /usr/bin/ratio.py
	install --mode=644 ./ratio.py.1 /usr/share/man/man1/
