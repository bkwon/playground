import xml.dom.minidom

def main():

    doc= xml.dom.minidom.parse("samplexml.xml");

    print("Node Name: ",doc.firstChild.tagName)

    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)

main()

