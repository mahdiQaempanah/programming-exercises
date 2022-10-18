import re
from Street import Street
from Student import Student
from Car import Car
from City import City


pattern = re.compile("^(Street|Car|Student|City) (json|csv) ([1-9][0-9]*)\s*$")
street, student, car, city = Street(), Student(), Car(), City()

while True:
    my_match = pattern.match(input())
    if my_match is None:
        print("Bad pattern.")
    else:
        entity_type = my_match.group(1)
        output_format = my_match.group(2)
        number_of_entity = int(my_match.group(3))
        if entity_type == "Street":
            print(street.to_json(number_of_entity) if output_format == "json" else street.to_cmv(number_of_entity))
        elif entity_type == "Student":
            print(student.to_json(number_of_entity) if output_format == "json" else student.to_cmv(number_of_entity))
        elif entity_type == "Car":
            print(car.to_json(number_of_entity) if output_format == "json" else car.to_cmv(number_of_entity))
        elif entity_type == "City":
            print(city.to_json(number_of_entity) if output_format == "json" else city.to_cmv(number_of_entity))