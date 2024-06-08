from config import HOME
import os
import xml.etree.ElementTree as ET
import os.path as osp
import xml.dom.minidom
def process_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    # Find all object elements
    objects = root.findall('object')
    car_objects = [obj for obj in objects if obj.find('name').text == 'car']
    if not car_objects:
        # If no car objects, set this as background class
        for obj in objects:
            root.remove(obj)
        background_object = ET.Element('object')
        ET.SubElement(background_object, 'name').text = 'background'
        ET.SubElement(background_object, 'pose').text = 'Unspecified'
        ET.SubElement(background_object, 'truncated').text = '0'
        ET.SubElement(background_object, 'difficult').text = '0'
        bndbox = ET.SubElement(background_object, 'bndbox')
        ET.SubElement(bndbox, 'xmin').text = '0'
        ET.SubElement(bndbox, 'ymin').text = '0'
        ET.SubElement(bndbox, 'xmax').text = '0'
        ET.SubElement(bndbox, 'ymax').text = '0'
        root.append(background_object)
    else:
        # Remove non-car objects
        for obj in objects:
            if obj.find('name').text != 'car':
                root.remove(obj)
    # Write the modified XML back to file with pretty print
    xml_str = ET.tostring(root, encoding='unicode')
    pretty_xml_as_str = minidom_prettify(xml_str)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(pretty_xml_as_str)
def minidom_prettify(xml_str):
    """Return a pretty-printed XML string for the Element."""
    rough_string = xml_str
    reparsed = xml.dom.minidom.parseString(rough_string)
    return '\n'.join([line for line in reparsed.toprettyxml(indent="    ").split('\n') if line.strip()])
def process_all_files(directory):
    for filename in os.listdir(directory):
        # print(filename)
        if filename.endswith(".xml"):
            file_path = os.path.join(directory, filename)
            process_xml_file(file_path)
if __name__ == "__main__":
    VOC_ROOT = osp.join(HOME, "data/VOCdevkit/")
    directory = osp.join(VOC_ROOT, "VOC2007/Annotations")
    process_all_files(directory)