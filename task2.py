def update_car_info(**kwargs):
    kwargs['is_available'] = True
    return kwargs


car_info = update_car_info(brand='Lamborgini', price=2000000)
print(car_info)