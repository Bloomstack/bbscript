import subprocess

def tests():
	"""Run all project unit tests"""
	subprocess.run(
		["coverage", "run", "--source", "bbscript", "-m", "unittest", "discover", "-s", "tests", "-p", "*_test.py"]
	)
	coverage()

def coverage():
	"""Run coverage reports"""
	subprocess.run(
		["coverage", "report", "-m"]
	)
