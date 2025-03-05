import os

def rotate_point_image_space(x, y):
    return y, 1 -x

def process_txt_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            out_path = '/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/2/labels/val/call2'
            with open(file_path, "r") as file:
                lines = file.readlines()
            

            newline = []
            for line in lines:
                splited = line.split(' ')
                x, y= rotate_point_image_space(float(splited[1]),float(splited[2]))
                line = f'{splited[0]} {x} {y} {splited[4][:-1]} {splited[3]}'
                newline.append(line)
                print(line)
            file_path1 = os.path.join(out_path, filename)
            with open(file_path1, "w") as file:
                file.writelines(newline)

folder_path = "/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/2/labels/val/call"  # مسیر را به مسیر پوشه خود تغییر دهید
process_txt_files(folder_path)
