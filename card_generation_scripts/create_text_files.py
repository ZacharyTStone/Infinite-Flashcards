import os

def create_blank_files():
    files = ['words.txt']

    for file in files:
        with open(file, 'w') as f:
            pass

def main():
    files_exist = all(os.path.isfile(file) for file in ['words.txt'])
    
    if files_exist:
        overwrite = input("Files already exist. Do you want to overwrite them? (yes/no): ").strip().lower()
        if overwrite == 'yes':
            create_blank_files()
            print("Files overwritten.")
        else:
            print("Files not overwritten.")
    else:
        create_blank_files()
        print("Files created.")

if __name__ == "__main__":
    main()
