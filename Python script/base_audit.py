import os

# Create class: DataShell
class DataShell:
  
	# Init method 
    def __init__(self, filename):
		# Set and initialize value of input arguments
        self.filename = filename
        self.ext = os.path.splitext(filename)

    # Get file type
    def file_ext(self):
        file, ext = os.path.splitext(self.filename)
        return ext

shell = DataShell('file.txt')
print(shell.filename)
print(shell.ext)
print(shell.file_ext())

"""
@todo

file delimiter
"""