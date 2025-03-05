import os


def process_txt_files(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, "r") as file:
                    lines = file.readlines()
                
                newline = []
                for line in lines:
                    splited = line.split(' ')
                    if int(splited[0]) == 8:
                        newline.append(f'{7} {splited[1]} {splited[2]} {splited[3]} {splited[4]}')
                with open(file_path, "w") as file:
                    file.writelines(newline)

folder_path = "/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/2/labels/val/eight" 
process_txt_files(folder_path)
