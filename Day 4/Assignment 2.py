km_to_m = lambda distance: distance * 1000
m_to_cm = lambda distance: distance * 100
cm_to_mm = lambda distance: distance * 10
ft_to_in = lambda distance: distance * 12
in_to_cm = lambda distance: distance * 2.54
km_to_ft = lambda distance: distance * 3280.84

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