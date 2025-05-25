import os

def replace_in_file(file_path, old_word, new_word):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    new_content = content.replace(old_word, new_word)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def rename_files_and_folders(root_dir, old_word, new_word):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in files:
            if name.endswith(('.py', '.txt', '.ini', '.md', '.json')):
                file_path = os.path.join(root, name)
                replace_in_file(file_path, old_word, new_word)

        for name in files:
            if old_word in name:
                os.rename(os.path.join(root, name), os.path.join(root, name.replace(old_word, new_word)))

        for name in dirs:
            if old_word in name:
                os.rename(os.path.join(root, name), os.path.join(root, name.replace(old_word, new_word)))

# نفذ التغيير على المجلد الحالي
rename_files_and_folders('.', 'fa', 'fa')
