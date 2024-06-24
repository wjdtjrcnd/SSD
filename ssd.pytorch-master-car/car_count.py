import os
import xml.etree.ElementTree as ET

def count_car_occurrences(xml_folder):
    car_count = 0
    total_count = 0

    # Iterate over all XML files in the specified folder
    for filename in os.listdir(xml_folder):
        if filename.endswith('.xml'):
            xml_file = os.path.join(xml_folder, filename)
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # Check if the XML file contains an <object> tag with <name>car</name>
            for obj in root.findall('object'):
                name = obj.find('name').text
                if name == 'car':
                    car_count += 1
                    break  # If 'car' is found once, count it and move to the next XML file
            
            total_count += 1

    return car_count, total_count

def calculate_car_ratio(xml_folder):
    car_count, total_count = count_car_occurrences(xml_folder)
    if total_count == 0:
        return 0.0
    print('number of cars: {}\nnumber of background: {}'.format(car_count, total_count-car_count))
    return car_count / total_count

# Example usage:
xml_folder = '/home/jehyeon/ssd/ssd.pytorch-master-car/data/VOCdevkit/CAR/Annotations'
car_ratio = calculate_car_ratio(xml_folder)
print(f"The ratio of XML files containing 'car' as the object name: {car_ratio:.2%}")
