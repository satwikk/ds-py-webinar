from pprint import pprint

datafp = open("data/raw_data1.csv","r")
raw_data_list = datafp.readlines()
datafp.close()

index_list = raw_data_list[0].replace("\r\n",'').split(',')
final_index_list = ['_'.join(x.split(' ')).replace('(','').replace(')','') for x in index_list]

processed_data = {}
processed_data["raw_records"] = []
processed_data_list = []
for raw_data in raw_data_list[1:]:
    temp_processed_data = raw_data.replace("\r\n",'').split(',')
    record = {}
    for (index, data) in zip(final_index_list, temp_processed_data):
        record[index] = data
    processed_data_list.append(record)

state_wise_count = {}

for patient_record in processed_data_list:
	if 'State_code' in patient_record.keys():
		if patient_record['State_code'] not in state_wise_count.keys():
			state_wise_count[patient_record['State_code']] = 0
		state_wise_count[patient_record['State_code']] += 1

pprint(state_wise_count)
