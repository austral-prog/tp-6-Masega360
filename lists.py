def remove_elements(list_to_remove_elements):
    largo = len(list_to_remove_elements)
    if largo >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    elif largo == 5:
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    elif largo <5 and largo > 0:
        del list_to_remove_elements[0]
    return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.append("Yellow")
    list_to_add_elements.insert(0, "Pink")
    return list_to_add_elements

def is_empty(list_to_check):
    if list_to_check == []:
        return True
    else: 
        return False
    
def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        value_1 = list_to_compare1[2]
        value_2 = list_to_compare2[2]
        if value_1 == value_2:
            return True
        else:
            return False
    else:
            return False
    
def list_of_lists(list_of_lists_to_modify):
    if (len(list_of_lists_to_modify[0]) >=3 and len(list_of_lists_to_modify[1]) > 4 and len(list_of_lists_to_modify[2]) > 2):
        list_of_lists_to_modify[0] = list_of_lists_to_modify[0][0:2]
        list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
        list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]
        return list_of_lists_to_modify
    elif (len(list_of_lists_to_modify[1]) <= 4 and len(list_of_lists_to_modify[1]) > 1  and len(list_of_lists_to_modify[2]) > 2):
        list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:len(list_of_lists_to_modify)]
        list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]
    elif (len(list_of_lists_to_modify[1]) <= 1):
        list_of_lists_to_modify[1] = []
    return list_of_lists_to_modify



        



        
    
