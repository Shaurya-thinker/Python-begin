""" import os

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}") """

from file_organiser.organizer import organize_folder  # Import the function from the module

if __name__ == "__main__":
    path = input("Enter the path to organize: ").strip()
    print(path)
    organize_folder(path)
    print("Folder organized successfully.")


