run:
    python quiz.py

setup: requirements.txt
    pip install os
	pip install time
	
clean:
	rm -rf __pycache__
	
clean_win:
	del __pycache__