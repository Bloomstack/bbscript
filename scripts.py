import subprocess

def tests():
	"""Run all project unit tests"""
	subprocess.run(
		["env/Scripts/python.exe", "-m", "unittest", "discover", "-s", "tests", "-p", "*_test.py"]
	)