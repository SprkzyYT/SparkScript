import subprocess

pop = input("Interpreter path: ")

# Open a new Command Prompt and run a Python script
subprocess.run(["start", "cmd", "/k", "python", pop], shell=True)