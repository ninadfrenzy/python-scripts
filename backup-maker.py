import os
import shutil

source_dir = ''
dest_dir = ''

source_dir = input('Enter a source directory')
dest_dir = input('Enter a destination directory')

def check_if_source_and_dest_exist(src, dest):
    if(os.path.isdir(src) and os.path.isdir(dest)):
        return True
    else:
        return False
def calculate_move_size(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += calculate_move_size(entry.path)
    return total//1024//1024
def move_all_files(src, dest):
    files_in_directory = os.listdir(src)
    for single_file in files_in_directory:
        file_path = os.path.join(src, single_file)
        print(file_path)
        shutil.move(file_path, dest)

def move_files(src, dest):
    if(check_if_source_and_dest_exist(src,dest)):
        total_size = calculate_move_size(src)
        confirm_move = input('total size is (Mb)'+str(total_size)+' are you sure? Y/N')
        if(confirm_move == 'Y'):
            move_all_files(src, dest)
            print('backup complete.')
    else:
        raise Exception('either source or destination does not exist')



move_files(source_dir, dest_dir)
        

