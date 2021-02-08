# -*- coding: utf-8 -*-
import xml.etree.ElementTree as xml
import re

def generateXML(filename):
    
    index = 0
    matrl = []
    with open('C:\\Users\\e485858\\Documents\\Work\\PROS\\AERO\\Todd\\HierLogs\\Material.txt',mode='r',buffering=500000,errors='ignore') as mat:
        for line in mat:
            matrl.append(line)   
    
    with open('C:\\Users\\e485858\\Documents\\Work\\PROS\\SFTP\\Aero\\MasterData\\Product\\_PRODUCT.20210122.xml',mode='r',buffering=50000,errors='ignore') as file:
        root = xml.Element('PRODUCT_Set')
        for line in file:
            # print(line.find('G197902-1'))
            # break
            # index += 1
            # if line =='':
            #     break
            for material in matrl:
            # material = 'MFM8791 1-137'
                idx = line.find(material)
                if idx >= 0:
                    print('Found',idx)
                    # print(line[idx+250:idx+450])
            # doc = xml.SubElement(root, 'PRODUCT_Record')
            # new_str = re.sub('[^a-zA-Z0-9\n\.\^\*\-\//]', ' ', line)
                # arr = list(line.split('\n'))
                # print(arr)
            # matnew = re.sub('[^a-zA-Z0-9\n\.\^\*\-\//]', ' ', arr[10])

            # if matnew+'\n' in material:
                # print(matnew)
        #         doc = xml.SubElement(root, 'PRODUCT_Record')
        #         END_ITEM = xml.SubElement(doc,'END_ITEM')
        #         Extraction_Time = xml.SubElement(doc,'Extraction_Time')
        #         LRU_FLAG = xml.SubElement(doc,'LRU_FLAG')
        #         LRU_INDICATOR = xml.SubElement(doc,'LRU_INDICATOR')
        #         MFG_CAGE_CODE = xml.SubElement(doc,'MFG_CAGE_CODE')
        #         PART_NUMBER = xml.SubElement(doc,'PART_NUMBER')
        #         PART_NUMBER_DESC = xml.SubElement(doc,'PART_NUMBER_DESC')
        #         PRICING_CODE = xml.SubElement(doc,'PRICING_CODE')
        #         PRIMARY_SUPPLIER_CODE = xml.SubElement(doc,'PRIMARY_SUPPLIER_CODE')
        #         PRODUCT_CLASS = xml.SubElement(doc,'PRODUCT_CLASS')
        #         PRODUCT_CLASS_DESC = xml.SubElement(doc,'PRODUCT_CLASS_DESC')
        #         PRODUCT_FAMILY = xml.SubElement(doc,'PRODUCT_FAMILY')
        #         PRODUCT_FAMILY_DESC = xml.SubElement(doc,'PRODUCT_FAMILY_DESC')
        #         PRODUCT_GROUP = xml.SubElement(doc,'PRODUCT_GROUP')
        #         PRODUCT_GROUP_DESC = xml.SubElement(doc,'PRODUCT_GROUP_DESC')
        #         PRODUCT_LINE = xml.SubElement(doc,'PRODUCT_LINE')
        #         PRODUCT_LINE_DESC = xml.SubElement(doc,'PRODUCT_LINE_DESC')
        #         PRODUCT_TYPE = xml.SubElement(doc,'PRODUCT_TYPE')
        #         PRODUCT_TYPE_DESC = xml.SubElement(doc,'PRODUCT_TYPE_DESC')
        #         SUPPLIER_CODE = xml.SubElement(doc,'SUPPLIER_CODE')
                
        #         END_ITEM.text = arr[13]
        #         Extraction_Time.text = "20200917 00:00:00"
        #         LRU_FLAG.text = 'N'
        #         LRU_INDICATOR.text = arr[12]
        #         MFG_CAGE_CODE.text = arr[16]
                
        #         # PART_NUMBER.text = matnew
        #         # PART_NUMBER_DESC.text = matnew+' || '+arr[11]
        #         PART_NUMBER.text = arr[10]
        #         PART_NUMBER_DESC.text = arr[10]+' || '+arr[11]
        #         PRICING_CODE.text = arr[15]
        #         PRIMARY_SUPPLIER_CODE.text = arr[17]
        #         PRODUCT_CLASS.text = 'PC-'+arr[0]
        #         PRODUCT_CLASS_DESC.text = 'PC-'+arr[0]+' || '+arr[1]
        #         PRODUCT_FAMILY.text = 'PF-'+arr[2]
        #         PRODUCT_FAMILY_DESC.text = 'PF-'+arr[2]+' || '+arr[3]
        #         PRODUCT_GROUP.text = 'PG-'+arr[4]
        #         PRODUCT_GROUP_DESC.text = 'PG-'+arr[4]+' || '+arr[5]
        #         PRODUCT_LINE.text = 'PL-'+arr[6]
        #         PRODUCT_LINE_DESC.text = 'PL-'+arr[6]+' || '+arr[7]
        #         PRODUCT_TYPE.text = 'PT-'+arr[8]
        #         PRODUCT_TYPE_DESC.text = 'PT-'+arr[8]+' || '+arr[9]
        #         SUPPLIER_CODE.text = arr[14]
    
        # tree = xml.ElementTree(root)
 
        # with open(filename,"wb") as fb:
        #     tree.write(fb)

import xmltodict        
def parsexml(filename):
    result = xmltodict.parse(filename)
    print(result)
    

if __name__ == "__main__":
    generateXML("C:\\Users\\e485858\\Documents\\Work\\Python\\Workspace\\AssignmentProjects\\HackerRank\\Files\\xml1.xml")
   # parsexml("C:\\Users\\e485858\\Downloads\\Sample.xml") 
   
   # create the file structure
    
    # create a new XML file with the results
    # mydata = xml.tostring(data)
    # myfile = open("C:\\Users\\e485858\\Documents\\Work\\Python\\Workspace\\AssignmentProjects\\HackerRank\\Files\\sample.xml", "w")
    # myfile.write(mydata)


