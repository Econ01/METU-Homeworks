import math

def volumeCalculator(radius, height):
    return ((math.pi*radius**2*height)/3)

def printAllSubsets(list1, list2):
    list_of_valid_lists = []
    set1 = set(list1)
    for l in range(len(list2)):
        set2 = set(list2[l])
        check = set2<=set1
        if check==True:
            list_of_valid_lists.append(list2[l])
    for l in range(len(list_of_valid_lists)):
        print(list_of_valid_lists[l], "\n")

def queryTxt(filename, mode, field, Value):
    age_list = []
    id_list = []
    job_list = []
    name_list = []
    surname_list = []
    index_numbers = []
    fID1 = open(filename, "r")
    for l in fID1:
        s = l.split()
        length = len(s)
        upper_limit = length-2
        id_list.append(int(s[0]))
        age_list.append(int(s[-1]))
        job_list.append(s[-2])
        name_list.append(s[1:upper_limit])
    for l in range(len(name_list)):
        surname_list.append(name_list[l][-1])
    if field=="ID number":
        field = id_list
    if field=="Name":
        field = name_list
    if field=="Surname":
        field = surname_list
    if field=="Job":
        field = job_list
    if field=="Age":
        field = age_list

    if (mode=="search"):
        if (field==name_list):
            for l in range(len(field)):
                for n in range(len(field[l])):
                    if field[l][n]==Value:
                        index_numbers.append(l)
        else:
            for l in range(len(field)):
                if field[l]==Value:
                    index_numbers.append(l)
        if (len(index_numbers)==0):
            print("Empty")
        for l in range(len(index_numbers)):
            index_number = index_numbers[l]
            print(id_list[index_number], " ".join(name_list[index_number]), job_list[index_number], age_list[index_number])

    if (mode=="sort by"):
        ordered_coppy = []
        ordered_coppy = field[:]
        if Value=="ascending":
            ordered_coppy.sort()
        if Value=="descending":
            ordered_coppy.sort(reverse=True)
        for n in range(len(ordered_coppy)):
                for l in range(len(field)):
                    if (ordered_coppy[n]==field[l]):
                        if (ordered_coppy[n]==ordered_coppy[n-1]):
                            break
                        index_number = l
                        print(id_list[index_number], " ".join(name_list[index_number]), job_list[index_number], age_list[index_number])
    fID1.close()

queryTxt("simplefile.txt", "sort by", "Job", "ascending")