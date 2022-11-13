from pathlib import Path

path = Path("EnterTain")
path.mkdir()
path.rmdir()
print(path.exists())

#Path.rmdir("EnterTain")
#path = Path("EnterTain")
#print(path.exists())
