run :
	python3 main.py

test :
	python3 -m unittest


clean :
	find . | grep -E "/__pycache__/$" | xargs rm -rf
	find . | grep -E "/__pycache__/" | xargs rm


