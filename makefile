
run :
	python3 -m quad_solver


test :
	python3 --version
	python3 -m unittest


clean :
	find . | grep -E "__pycache__$$" | xargs rm -rf


