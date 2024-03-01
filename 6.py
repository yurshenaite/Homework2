weight = float(input())
height = float(input())
weight_kg = weight * 0.454
height_m = height * 0.0254
imt = weight_kg / (height_m ** 2)
print(f'Индекс массы тела равен {round(imt, 2)}')