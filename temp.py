import os
fromtranspath = r"C:\Users\AnZhou\Downloads\temp\moldflow\fromtrans"

# path_with_date = os.path.join(fromtranspath, os.listdir(fromtranspath)[0])
path_with_date = max(os.listdir(fromtranspath))
absolute_path_with_date = os.path.join(fromtranspath, path_with_date)
print(absolute_path_with_date)
