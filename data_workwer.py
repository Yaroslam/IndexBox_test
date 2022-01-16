import numpy as np


def create_data_dicts_by_rows(data, rows):
    new_data = []
    for i in data:
        new_data_dict = dict(zip(rows, i))
        new_data.append(new_data_dict)
    return new_data


def count_world_res_by_year(data):
    years_res = {}
    for i in data:
        year = i["year"]
        contry_res = i["res"]
        if year not in years_res.keys():
            if contry_res == None:
                years_res[year] = np.NAN
            else:
                years_res[year] = contry_res
        elif contry_res == None and years_res[year] == np.NAN:
            continue
        elif contry_res == None and years_res[year] != np.NAN:
            years_res[year] += 0
        elif contry_res != None and years_res[year] == np.NAN:
            years_res[year] = contry_res
        elif contry_res != None and years_res[year] != np.NAN:
            years_res[year] = contry_res

    return years_res


def create_data_first_data_to_dataframe(factor, years_res):
    result_data = []

    for i in years_res:
        part_of_data = [factor, i, years_res[i]]
        result_data.append(part_of_data)
    return result_data


def heapify(data, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and data[left_child][1] > data[largest][1]:
        largest = left_child

    if right_child < heap_size and data[right_child][1] > data[largest][1]:
        largest = right_child

    if largest != root_index:
        data[root_index][1], data[largest][1] = data[largest][1], data[root_index][1]

        heapify(data, heap_size, largest)


def fetch_right_data(data, right_params):
    lenght = len(data)
    ind = 0
    while ind < lenght - 1:
        for keys in right_params:
            if data[ind][keys] != right_params[keys]:
                lenght = len(data)
                data.pop(ind)
                ind-=1
        ind+=1

    return data




def heap_sort(data):
    n = len(data)

    for i in range(n, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)


def calculate_new_factor_res(facrotrs, reses, divisible_f, divider_f, years):
    divisible_f_ind = facrotrs.index(divisible_f)
    divider_f_ind = facrotrs.index(divider_f)

    lenght = len(facrotrs) - 1
    new_factor_dict = {}

    if divider_f_ind > divisible_f_ind:
        while (divider_f_ind <= lenght) and (facrotrs[divider_f_ind] == divider_f) and (
                facrotrs[divisible_f_ind] == divisible_f):
            new_factor_dict[years[divider_f_ind]] = reses[divisible_f_ind]/reses[divider_f_ind]
            divisible_f_ind+=1
            divider_f_ind+=1

    else:
        while (divisible_f_ind <= lenght) and (facrotrs[divider_f_ind] == divider_f) and (
                facrotrs[divisible_f_ind] == divisible_f):
            new_factor_dict[years[divider_f_ind]] = reses[divisible_f_ind] / reses[divider_f_ind]
            divisible_f_ind += 1
            divider_f_ind += 1

    return new_factor_dict

def parse_dataframe_data(data, key1='-', key2='-', key3='-'):
    first_dim = list(data[0])
    sec_dim = list(data[1])
    third_dim = list(data[2])
    res = [[],[],[]]

    if key1 != '-':
        ind = first_dim.index(key1)
        while ind < len(first_dim) and first_dim[ind] == key1:
            res[0].append(key1)
            res[1].append(sec_dim[ind])
            res[2].append(third_dim[ind])
            ind+=1

    #another 7 variants of keys value

    return res







def calculate_CAGR(start_val, end_val, count_of_years):
    CAGR_base = end_val/start_val
    CAGR_degree = 1/count_of_years

    return (CAGR_base**CAGR_degree)-1




