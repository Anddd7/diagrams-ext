demo:
	python main.py
	# code dist/demo.png

test:
	python -m unittest tests/*.py -v  

build: 
	poetry build