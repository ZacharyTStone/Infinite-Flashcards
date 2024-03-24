import os

def create_blank_files():
    base_path = os.path.dirname(__file__)  # 追加された行
    files = [os.path.join(base_path, 'words.txt')]  # 変更された行

    for file in files:
        with open(file, 'w') as f:
            pass

def main():
    base_path = os.path.dirname(__file__)  # 追加された行
    files_exist = all(os.path.isfile(os.path.join(base_path, 'words.txt')) for file in ['words.txt'])  # 変更された行
    
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
