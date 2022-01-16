import numpy as np
import pandas as pd

# A = np.array([1, 1, 2, 2, 'three', 'three'])
# B = np.array(['start', 'end']*3)
# C = [[42],[42],[42],[42],[42],[42]]
# max_len = max(len(sublist) for sublist in C)
# for sublist in C:
#     sublist.extend([np.nan] * (max_len - len(sublist)))
# C = np.array(C)
# df = pd.DataFrame(data=C.T, columns=pd.MultiIndex.from_tuples(zip(A,B)))

def prepare_data(data, first_dim=0, sec_dim=1, third_dim=2):
        first_dimension_data= []
        sec_dimension_data = []
        third_dimension_data = []
        for i in data:
            first_dimension_data.append(i[first_dim])
            sec_dimension_data.append(i[sec_dim])
            third_dimension_data.append([i[third_dim]])

        return[np.array(first_dimension_data), np.array(sec_dimension_data), np.array(third_dimension_data)]

def create_3d_dataframe(dimensions_data):
        first_dimension_data = dimensions_data[0]
        sec_dimension_data = dimensions_data[1]
        third_dimension_data = dimensions_data[2]


        three_d_dataframe = pd.DataFrame(data=third_dimension_data.T,
                                         columns=pd.MultiIndex.from_tuples(zip(first_dimension_data, sec_dimension_data)))

        return three_d_dataframe

def parse_3d_dataframe(dataframe, first_dim_key="-", sec_dim_key="-", third_dim_key="-"):
        first_dim = []
        second_dim = []
        third_dim = []
        for i in dataframe:
            first_dim.append(i[0])
            second_dim.append(i[1])
            dim1 = i[0]
            dim2 = i[1]
            third_dim.append(dataframe[dim1][dim2][0])

        return [np.array(first_dim), np.array(second_dim), np.array(third_dim)]
    
def merge_3d_dataframe(dataframe_first, dataframe_sec):
        data_to_merge = parse_3d_dataframe(dataframe_first)
        data_merged = parse_3d_dataframe(dataframe_sec)

        data_first = compare_data(data_to_merge)
        data_sec = compare_data(data_merged)

        data = []

        for i in data_first:
            data.append(i)

        for i in data_sec:
            data.append(i)

        data = prepare_data(data,0,1,2)
        new_dataframe = create_3d_dataframe(data)

        return new_dataframe

def compare_data(data):
        lenght = len(data[0]) - 1
        res_data = []
        count_of_parts = 0

        while count_of_parts <= lenght:
            part_of_data = [data[0][count_of_parts], data[1][count_of_parts],
                            data[2][count_of_parts]]
            res_data.append(part_of_data)
            count_of_parts += 1

        return res_data
        
