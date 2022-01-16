from DB_worker import *
from data_workwer import *
from Pandas_worker import *


right_data = {"bs": 0, "partner": None, "state": None}
connect = Database_worker('test.db').open_connect()
Test_table = Test_table_Worker('testidprod', connect)
period_data = Test_table.get_rows_by_factor(1)
names = Test_table.get_all_column_names()

frame_1_rows = create_data_dicts_by_rows(period_data, names)
frame_1_rows = fetch_right_data(frame_1_rows, right_data)
frame_1_res = count_world_res_by_year(frame_1_rows)
frame_1_first_data = create_data_first_data_to_dataframe(1, frame_1_res)
heap_sort(frame_1_first_data)
frame_1_first_data = prepare_data(frame_1_first_data)
first_dataframe = create_3d_dataframe(frame_1_first_data)

period_data = Test_table.get_rows_by_factor(2)
frame_2_rows = create_data_dicts_by_rows(period_data, names)
frame_2_rows = fetch_right_data(frame_2_rows, right_data)
frame_2_res = count_world_res_by_year(frame_2_rows)
frame_2_first_data = create_data_first_data_to_dataframe(2, frame_2_res)
heap_sort(frame_2_first_data)
frame_2_first_data = prepare_data(frame_2_first_data)
sec_dataframe = create_3d_dataframe(frame_2_first_data)

third_dataframe = merge_3d_dataframe(first_dataframe, sec_dataframe)
third_dataframe_data = parse_3d_dataframe(third_dataframe)

six_factor_res = calculate_new_factor_res(list(third_dataframe_data[0]), list(third_dataframe_data[2]), 2, 1,
                                          list(third_dataframe_data[1]))
frame_6_first_data = create_data_first_data_to_dataframe(6, six_factor_res)
heap_sort(frame_6_first_data)
frame_6_first_data = prepare_data(frame_6_first_data)
six_dataframe = create_3d_dataframe(frame_6_first_data)

third_dataframe = merge_3d_dataframe(third_dataframe, six_dataframe)


print(third_dataframe)
third_dataframe.to_excel("test.xlsx")