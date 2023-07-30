def get_file():
    costume_file = open("costumes.txt","r")
    file_data = costume_file.readlines()
    costume_file.close()
    return file_data

def get_dictionary(file_data):
    info = {}
    for x in range(len(file_data)):
        info[x + 1] = file_data[x].replace("\n","").split(",")
    return info

def set_file(file_data):
    costume_file = open("costumes.txt","w")
    for key,data in file_data.items():
        costume_file.write(",".join(data)+"\n")
    costume_file.close()

def print_costumes():
    file_data = get_dictionary(get_file())
    print("S.N.", "\t", "COSTUME NAME", "\t\t\t\t", "Brand","\t\t","PRICE","\t\t","STOCK")
    print("===========================================================================================")

    for key, value in file_data.items():
        print(key,"\t",value[0],"\t",value[1],"\t",value[2],"\t",value[3])

print(get_dictionary(get_file()))
