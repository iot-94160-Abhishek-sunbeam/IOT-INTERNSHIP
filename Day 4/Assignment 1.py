def km_to_m(distance):
    return distance * 1000

def m_to_cm(distance):
    return distance * 100

def cm_to_mm(distance):
    return distance * 10

def ft_to_in(distance):
    return distance * 12

def in_to_cm(distance):
    return distance * 2.54

def distance_convert(distance, conversion_type, conversion_func):
    result = conversion_func(distance)
    from_unit,to_unit=conversion_type.split(' to ')
    print(f"{distance} {from_unit} is {result} {to_unit}")

distance=float(input("enter distance in kilometer= "))
distance_convert(distance,"km to m" , km_to_m)
distance=km_to_m(distance)
distance_convert(distance,"m to cm", m_to_cm)
distance=m_to_cm(distance)
distance_convert(distance, "m to mm", cm_to_mm)
distace=cm_to_mm(distance)

distance_ft = distance
distance_convert(distance, "ft to in", ft_to_in)
distance=-ft_to_in(distance_ft)
distance_convert(distance,"in to cm ", in_to_cm)
distance=in_to_cm(distance_ft)
