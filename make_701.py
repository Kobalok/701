import pandas as pd
import time
import xml.etree.ElementTree as ET
from datetime import datetime as dt

df_orders = pd.read_excel('11102024_701.xlsx')
print(df_orders.head())
print(df_orders.index)
print(df_orders.columns)
today = dt.today()
mtime=dt.now()
#print(mtime.strftime("%Y-%m-%dT%H:%M:%S+03:00"))
#print("Today's date:", today)
xmlasastring="""<?xml version="1.0" encoding="UTF-8"?>
<documents xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.38">
  <accept action_id="701">
    <subject_id></subject_id>
    <counterparty_id></counterparty_id>
    <operation_date>dateT17:43:39+03:00</operation_date> 
    <order_details>
    </order_details>
  </accept>
</documents>
"""

def createXML(filename,param1,param2):
    """
    Создаем xml файл
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    for msubject_id in root.iter('subject_id'):
        msubject_id.text=param1
    for mcounterparty_id in root.iter('counterparty_id'):
        mcounterparty_id.text='444'
    for moperation_date in root.iter('operation_date'):
        moperation_date.text=mtime.strftime("%Y-%m-%dT%H:%M:%S+03:00")
    tree.write('out.xml')

    mdocuments = ET.Element('new_tag')
    mdocuments.set('attribute_name', 'attribute_value')
    mdocuments.text = 'element_text'
    root.append(mdocuments)
    tree.write('updated.xml')
    """
    Редактируем XML файл.
    """
  
    
    
    #tree = ET.ElementTree(file=filename)
    #root = tree.getroot()
    
    #for subject_id in root.iter("subject_id"):
    #    subject_id.text = "11111111"
    
    #tree = ET.ElementTree(root)
    #with open("updated.xml", "w", encoding='utf-8') as f:
        
      
 
if __name__ == "__main__":
    createXML("701.xml","123","456")



    