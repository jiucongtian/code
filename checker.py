import xml.dom.minidom

#---------------functions def---------------------------------------------------------
def getSkinName(skinNode):
    atts = skinNode.getElementsByTagName('att')
    for att in atts:
        if att.getAttribute("name") == 'Name':
            return att.getAttribute("value")

def isEqualAtt(attNode1, attNode2):
    equal = True
    if not attNode1.getAttribute("name") == attNode2.getAttribute("name"):
        equal = False
    if not attNode1.getAttribute("value") == attNode2.getAttribute("value"):
        equal = False
    if not attNode1.getAttribute("type") == attNode2.getAttribute("type"):
        equal = False
    return equal
		
def compareSkin(skin1, skin2):
    isSameSkin = True
    atts1 = skin1.getElementsByTagName('att')
    atts2 = skin2.getElementsByTagName('att')

    index = 0
    for index in range(len(atts1)):
        if not isEqualAtt(atts1[index], atts2[index]):
            if not atts1[index].getAttribute('name') == 'Name':
                isSameSkin = False
                break
    #if isSameSkin:
    #    output skin name
    #    print atts1[0].getAttribute('value'), '==', atts2[0].getAttribute('value')
    return isSameSkin

def updateElements(dom):
    root = dom.documentElement
    return root.getElementsByTagName('skin')

#---------------functions-------------------------------------------------------------
file_object = open('output.log','w')

#open skin.xml file.
dom = xml.dom.minidom.parse('skin.xml')
root = dom.documentElement
skins = root.getElementsByTagName('skin')
skinsNumber = len(skins)

totalReduplicate = 0

while(len(skins) >= 2):
    foundSame = False
    firstSkin = skins[0]
    skins.remove(skins[0])
    print 'scan skin ', getSkinName(firstSkin)

    index = 0
    while (index < len(skins)):
        if compareSkin(firstSkin, skins[index]):
            if not foundSame:
                totalReduplicate += 1
                file_object.write(getSkinName(firstSkin))
                foundSame = True
            file_object.write(' ,')
            totalReduplicate += 1
            file_object.write(getSkinName(skins[index]))
            skins.remove(skins[index])
        else:
            index += 1
    if foundSame:
        file_object.write('\n')
        
print 'total skins number is:', skinsNumber
print 'total reduplicate mount:', totalReduplicate
print 'scan finished'

file_object.close()




            

    
