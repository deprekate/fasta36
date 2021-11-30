
all:
	python3 setup.py install --user

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr fasta36.egg-info/
	pip uninstall fasta36 -y
