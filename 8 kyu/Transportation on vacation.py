def rental_car_cost(d):
  if d < 4:
    return d*40
  elif d < 7:
    return d*40-20
  else:
    return d*40-50
