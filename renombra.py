
from pandas import read_excel
from shutil import copyfile
from tqdm import tqdm

tqdm.pandas(desc = "Archivos: ")
print("Inicializando ...")

nm_excel = "./nombres.xlsx"
df = read_excel(nm_excel)

df.progress_apply(lambda row: copyfile("./input/"+row[0], "./output/"+row[1]), axis=1)
