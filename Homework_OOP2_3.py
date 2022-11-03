
def dict_file (name, dict_f):
    with open(name, 'r', encoding='utf-8') as f:
        text = f.readlines()
        f.seek(0)
        count = sum(1 for line in f)
        dict_f[count] = [name, text]
    return dict_f


files_dict = {}
files_dict = dict_file('1.txt', files_dict)
files_dict = dict_file('2.txt', files_dict)
files_dict = dict_file('3.txt', files_dict)

sorted_dict = dict(sorted(files_dict.items(), key=lambda x: x[0]))

my_file = open("file_new.txt", "w+",  encoding='utf-8')
for key, val in sorted_dict.items():
    my_file.write(val[0]+"\n")
    my_file.write(str(key)+"\n")
    my_file.write('\n'.join(val[1])+"\n")
my_file.close()







