#FILE MANAGEMENT APP IN PYTHON.
import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File name {filename}:Created successfully.")
    
    except FileExistsError:
        print(f"File has{filename}:already exits.")

    except Exception as E:
        print(f"AN Error occurred.")

def view_all_files():
    files = os.listdir()
    if not files:
        print("file not found.")
    else:
        print("File have found.")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File{filename} has been deleted successfully.")
    except FileNotFoundError:
        print("file not found")
    
    except Exception as e:
        print("An error occured.")

def read_file(filename):
    try:
        with open("sample.txt","r") as f:
            content = f.read()
            print("content {filename}:\n{content}")
    
    except FileNotFoundError:
        print("file not found")
    
    except Exception as e:
        print('an error occured.')

def edit_file(filename):
    try:
        with open("sample.txt","a") as f:
            content = input("enter to add data = ")
            f.write(content + "\n")
            print(f"File{filename} has been edited successfully.")

    except FileNotFoundError:
        print("{filename} file not found")

    except Exception as e:
        print('an error occurred.')

def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1 : create file")
        print("2 : view all file")
        print("3 : delete file")
        print("4 : read file")
        print("5 : edit file")
        print("6 : EXIT")

        choice = input("input your choice(1-6) = ")

        if choice == "1":
            filename = input("enter the file-name to create = ")
            create_file(filename)

        elif choice == "2":
            view_all_files()

        elif choice == "3":
            filename = input("enter the file-name to delete the file =  ")
            delete_file(filename)

        elif choice == "4":
            filename = input("enter the file-name to read = ")
            read_file(filename)

        elif choice == "5":
            filename = input("enter the file-name you want to edit = ")
            edit_file(filename)

        elif choice == "6":
            print("Closing the App....")
            break

        else:
            print("invalid input!")

if __name__ == "__main__":
    main()