import global_variable
import json


def classification_storage(data):
    data_json = data.loc[:,['Job_link', 'Error_Type' ]]
    data_id = data['Job_ID']
    data_dic=data_json.to_dict( orient='index')
    
    for key in range(len(data_dic)):
        temp = data_dic[key]
        new_key = data_id[key]
        del data_dic[key]
        data_dic[new_key] = temp
        
    upload_file_name = global_variable.upload_dir_name + "Label_Rhel_" + global_variable.timestr + ".json"
    with open(upload_file_name, 'w') as fp:
        json.dump(data_dic, fp)