import os
import pandas as pd
import time
import xml.etree.ElementTree as ET
from datetime import datetime as dt


mPapka=''
mApt=''
tmp=''
mtime=dt.now()
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


def createXML(filename,param1,param2,msgtin):
    
    """
    Редактируем XML файл.
    """
    if os.path.exists(filename):
        tree  = ET.parse(filename)
        root = tree.getroot()
        for child in root.iter('order_details'):
            item = ET.SubElement(child, 'sgtin')
            item.text = msgtin
        tree.write(filename)
    else:
        """
        Создаем xml файл
        """
        tree  = ET.ElementTree(ET.fromstring(xmlasastring))
        root = tree.getroot()
        for msubject_id in root.iter('subject_id'):
            msubject_id.text=param1
        for mcounterparty_id in root.iter('counterparty_id'):
            mcounterparty_id.text=param2
        for moperation_date in root.iter('operation_date'):
            moperation_date.text=mtime.strftime("%Y-%m-%dT%H:%M:%S+03:00")
        for child in root.iter('order_details'):
            item = ET.SubElement(child, 'sgtin')
            if item.text != msgtin:
                item.text = msgtin
        tree.write(filename)

    #msgtin = ET.Element('new_tag')
    #msgtin.set('attribute_name', 'attribute_value')
    #msgtin.text = 'element_text'
    #root.append(mdocuments)
    
    
  

def delProbel(mStr):
    return str(mStr).replace(' ','')

def FindUL(mStr):
    if mStr.find("Ригла")!=-1:
        mUL='Ригла'
    if mStr.find("Оз")!=-1:
        mUL='Аптечная сеть Оз'
    if mStr.find("здоров")!=-1:
        mUL='Будь здоров'
    if mStr.find("Ригла-МО")!=-1:
        mUL='Ригла-МО'
    if mStr.find("МР_ЗДОРОВЬЕ")!=-1:
        mUL='МР_ЗДОРОВЬЕ'
    if mStr.find("Гранд-Здоровья")!=-1:
        mUL='Гранд-Здоровья'
    if mStr.find("Фармасия")!=-1:
        mUL='Фармасия'
    if mStr.find("АВРОРА")!=-1:
        mUL='АВРОРА'
    if mStr.find("Вита")!=-1:
        mUL='Вита Фарм'



    return mUL
     



if __name__ == "__main__":
    excel_data = pd.read_excel('11102024_701.xlsx',dtype=object)
    data = pd.DataFrame(excel_data, columns=['РК', 'Аптека', 'SGTIN','MD аптеки','MD поставщика'])
    #print(data.head())
    for row in data.itertuples():
        mPapka=FindUL(delProbel(row[1]))
        mApt=delProbel(row[2])
        mSGTIN=delProbel(row[3])
        MDa=delProbel(row[4])
        MDp=delProbel(row[5])
        if os.path.isdir(mPapka):
            print("Папка существует!")
        else:
            os.mkdir(mPapka)
        createXML(mPapka+'/'+mApt+'.xml',MDa,MDp,mSGTIN)
                    
        
        