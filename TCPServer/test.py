import xml.etree.ElementTree as ET


#xml_string = '''<?xml version="1.0" encoding="UTF-8"?><sensorReading><StationID type ="int">9</StationID><CarrierID type ="int">16</CarrierID><time><DateAndTime type ="string"> DateAndTime </DateAndTime></time></sensorReading>'''

xml_string = '''<?xml version="1.0" encoding="UTF-8"?><sensorReading><StationID type ="int">9</StationID><CarrierID type ="int">15</CarrierID><DateAndTime type ="string">DT#2023-5-25-13:58:57</DateAndTime></sensorReading>'''



sensordata = ET.fromstring(xml_string)

StationID_element = sensordata.find('StationID')
StationIDTag = StationID_element.tag
StationID = StationID_element.text
CarrierID_element = sensordata.find('CarrierID')
CarrierIDTag = CarrierID_element.tag
CarrierID = CarrierID_element.text
DateAndTime_element = sensordata.find('DateAndTime')
DateAndTimeTag = DateAndTime_element.tag
DateAndTime = DateAndTime_element.text.split("-")
DTyear = DateAndTime[0].split("#")
Year = DTyear[1]
Month = DateAndTime[1]
Day = DateAndTime[2]
TimeStamp = DateAndTime[3]
Time = DateAndTime[3].split(":")
Hour = Time[0]
Min = Time[1]
Sek = Time[2]




for x in sensordata:
    if x.tag == "DateAndTime":
        datesplit = x.text.split("-")
        print(datesplit)



    print("Tag: ", x.tag)
    print("Value: ", x.text)
