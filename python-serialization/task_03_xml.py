#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file."""
    
   
    root = ET.Element("data")
    
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  
    
   
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary."""
    
   
    tree = ET.parse(filename)
    root = tree.getroot()
    
    
    data = {}
    for child in root:
    
        data[child.tag] = child.text
    
    return data
