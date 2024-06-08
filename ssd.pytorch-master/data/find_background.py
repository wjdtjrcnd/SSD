from config import HOME
import os
import xml.etree.ElementTree as ET
import os.path as osp

def process_xml_file(file_path):
    file_path_parsed = file_path.split('/')
    xml = file_path_parsed[-1]
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Find all object elements
    objects = root.findall('object')
        # Remove non-car objects
    for obj in objects:
        if obj.find('name').text == 'background':
            print(xml)

            
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