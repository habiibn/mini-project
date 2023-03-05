import os
import math
import random
import re
import sys

# The function is expected to return a STRING_ARRAY
# The function accepts following parameters
# 1. INTEGER N
# 2. STRING_ARRAY bom

def minesweeper(N, bom):
    # 1. Cek lokasi dari bom
    # 2. Cek apakah bom berada di sisi samping
    # 3. Assign apakah angka 1 di 1 grid jarak dari bom
    # 4. Apabila terdapat angka 1 di sekitar beberapa bom, maka dijumlahkan
    
    if (N > 50):
        print("Jumlah bom melebihi 50")
        pass

