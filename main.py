from rembg import remove
from PIL import Image
import os

# input_path = 'D:\\tung\python\\remove-bg\\before\\ikan4.png'
input_path = 'D:\\tung\python\\remove-bg\\caca\\'
output_path = 'D:\\tung\\python\\remove-bg\\after\\'
index_list = []
index_list = os.listdir(input_path)

index_awal = 0
index_akhir = 5
for x in range(index_awal, index_akhir):
    basename = os.path.basename(index_list[x])
    input = Image.open(input_path + str(basename))
    output = remove(input)
    output.save(output_path + str(basename))




# output_path = 'D:\\tung\\python\\remove-bg\\after\\ikan4.png'

# input = Image.open(input_path)

# output = remove(input)

# output.save(output_path)