run_test:
	pytest -s -rx --showlocals tests/test_try.py
	# pytest -s -rx --showlocals  --pdb
prepare_data:
	python ./src/ml_ops_mnist/data.py
