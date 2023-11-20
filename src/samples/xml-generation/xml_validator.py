from lxml import etree


def validar(xml_path: str, xsd_path: str) -> bool:
    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result


def validator() -> str:
    xml_path = 'C:/Users/crist/Downloads/csvtoxml.xml'
    xsd_path = '/usr/data/result.xsd'

    if validar(xml_path, xsd_path):
        return "O XML criado é válido"
    else:
        return "O XML criado não é válido"


if __name__ == "__main__":
    validator()