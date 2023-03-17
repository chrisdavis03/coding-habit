import xml.etree.ElementTree as ET

#https://www.datacamp.com/tutorial/python-xml-elementtree

tree = ET.parse('./data/XUMO_BabyEinstein_US_mRSS.xml')
root = tree.getroot()

def iterate_direct_subelements(element):
    for child in element:
        print (child.tag, child.attrib)

def iterate_all_subelements(element): 
    [print (elem.tag, elem.attrib) for elem in root.iter()]

def search_element(root):
    for element in root.iter('item'):
        [print (sub) for sub in element]

if __name__ == '__main__':
    #for testing different functions
    # iterate_direct_subelements(root)
    # iterate_all_subelements(root)
    search_element(root)