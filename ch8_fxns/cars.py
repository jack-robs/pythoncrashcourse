#16.09.2018
 
"""
1) fxn to store car information in a dict cars{}
2) params: manufacturer, model name, **keyvals
3) call fxn w/ at least 2 **keyvals
4) print dict 
"""

def car_info(manufacturer, model_name, **addit_info):
    car_dict = {}
    car_dict['maker'] = manufacturer
    car_dict['model'] = model_name
    
    for k, v, in addit_info.items():
        car_dict[k] = v
    
    return car_dict


new_dict = car_info('subaru', 'outback', color='blue', drive='awd')
print(new_dict)
