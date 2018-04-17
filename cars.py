def cars(maker , model, **car_info):
    """Takes info about car maker & model and other variable arguments and
    returns a dictionary with the input info"""
    car_detail = {}
    car_detail['manufacturer'] = maker
    car_detail['model_name'] = model
    for key ,value in car_info.items():
        car_detail[key] = value
    return car_detail
    
car = cars(color = 'violet' , type = 'sedan' , maker = 'subaru',model = 'BRZ')


print(car)

        
