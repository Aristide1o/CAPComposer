'''
CAP  XML to Python object de/serialization

This code:
    - serializes a Python object into a CAP XML document
    - de-serializes a CAP XML document into a Python object
'''

__author__ = 'Aristide'

import xml.etree.ElementTree as etree
from xml.etree.ElementTree import ElementTree

class CAP():
    def __init__( self ):
        self.tree = ElementTree() # the etree structure


    def serialize(self):
        '''
        creates a XML string representation of the encapsulated etree
        '''
        return etree.tostring(self.tree.getroot())


    def parse(self, xmlString):
        '''
        processes XML string into the Python object
        '''
        tempTree = etree.fromstring(xmlString)
        print tempTree
        return self


def main():
    test_xml = '''
    <alert xmlns="urn:oasis:names:tc:emergency:cap:1.2">
        <identifier>KSTO1055887203</identifier>
        <sender>KSTO@NWS.NOAA.GOV</sender>
        <sent>2003-06-17T14:57:00-07:00</sent>
        <status>Actual</status>
        <msgType>Alert</msgType>
        <scope>Public</scope>
        <info>
            <category>Met</category>
            <event>SEVERE THUNDERSTORM</event>
            <responseType>Shelter</responseType>
            <urgency>Immediate</urgency>
            <severity>Severe</severity>
            <certainty>Observed</certainty>
            <eventCode>
                <valueName>SAME</valueName>
                <value>SVR</value>
            </eventCode>
            <expires>2003-06-17T16:00:00-07:00</expires>
            <senderName>NATIONAL WEATHER SERVICE SACRAMENTO CA</senderName>
            <headline>SEVERE THUNDERSTORM WARNING</headline>
            <description>AT 254 PM PDT...NATIONAL WEATHER SERVICE DOPPLER RADAR INDICATED A SEVERE
            THUNDERSTORM OVER SOUTH CENTRAL ALPINE COUNTY...OR ABOUT 18 MILES SOUTHEAST OF KIRKWOOD...MOVING
            SOUTHWEST AT 5 MPH. HAIL...INTENSE RAIN AND STRONG DAMAGING WINDS ARE LIKELY WITH THIS
            STORM.</description>
            <instruction>TAKE COVER IN A SUBSTANTIAL SHELTER UNTIL THE STORM PASSES.</instruction>
            <contact>BARUFFALDI/JUSKIE</contact>
            <area>
                <areaDesc>EXTREME NORTH CENTRAL TUOLUMNE COUNTY IN CALIFORNIA, EXTREME NORTHEASTERN
            CALAVERAS COUNTY IN CALIFORNIA, SOUTHWESTERN ALPINE COUNTY IN CALIFORNIA</areaDesc>
                <polygon>38.47,-120.14 38.34,-119.95 38.52,-119.74 38.62,-119.89 38.47,-120.14</polygon>
                <geocode>
                    <valueName>SAME</valueName>
                    <value>006109</value>
                </geocode>
                <geocode>
                    <valueName>SAME</valueName>
                    <value>006009</value>
                </geocode>
                <geocode>
                    <valueName>SAME</valueName>
                    <value>006003</value>
                </geocode>
            </area>
        </info>
    </alert>
    '''

    print test_xml

    capObj = CAP()

    parsed = capObj.parse(test_xml)

    print parsed
    
if __name__ == '__main__':
    main()