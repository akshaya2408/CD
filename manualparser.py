import xml.etree.ElementTree as ET


class ParseTreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

    def __repr__(self):
        return f"ParseTreeNode(value={self.value}, children={self.children})"


def parse_xml(input_xml):
    tree = ET.ElementTree(ET.fromstring(input_xml))
    root = tree.getroot()

    def recursive_parse_element(element):
        children = [recursive_parse_element(child) for child in element]

        if children:
            return ParseTreeNode(element.tag, children)
        else:
            return ParseTreeNode(element.tag, [element.text])

    return recursive_parse_element(root)


def parse_list(input_list):
    if isinstance(input_list, list):
        if len(input_list) == 3 and isinstance(input_list[0], int) and isinstance(input_list[2], int):
            return ParseTreeNode(input_list[1], [
                ParseTreeNode(str(input_list[0])),
                ParseTreeNode(str(input_list[2]))
            ])
        else:
            return ParseTreeNode("Unknown", [ParseTreeNode(str(item)) for item in input_list])
    else:
        return ParseTreeNode("Invalid", [])


xml_input = """
<expr>
    <num>3</num>
    <op>+</op>
    <num>5</num>
</expr>
"""

list_input = [3, "+", 5]

print("Roll no: 160123733004")

xml_tree = parse_xml(xml_input)
print("XML Parse Tree:")
print(xml_tree)

list_tree = parse_list(list_input)
print("\nList Parse Tree:")
print(list_tree)