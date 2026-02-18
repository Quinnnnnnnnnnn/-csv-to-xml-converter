# csv_to_xml.py
import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

def csv_to_xml(csv_path, xml_path, root_name='data', row_name='row'):
    """
    将CSV文件转换为XML格式
    
    参数:
        csv_path: CSV文件路径
        xml_path: 输出XML文件路径
        root_name: XML根节点名称
        row_name: 每行数据的节点名称
    """
    # 检查CSV文件是否存在
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV文件不存在: {csv_path}")
    
    # 创建XML根元素
    root = ET.Element(root_name)
    
    # 读取CSV文件
    with open(csv_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row_data in reader:
            # 为每行创建子元素
            row_element = ET.SubElement(root, row_name)
            for key, value in row_data.items():
                # 创建字段元素
                field = ET.SubElement(row_element, key.strip())
                field.text = str(value).strip() if value else ''
    
    # 美化XML输出
    xml_str = ET.tostring(root, encoding='utf-8')
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent='  ', encoding='utf-8')
    
    # 写入文件
    with open(xml_path, 'wb') as f:
        f.write(pretty_xml)
    
    print(f"✅ 转换完成！XML文件已保存至: {xml_path}")

if __name__ == '__main__':
    # 示例用法
    csv_to_xml('input.csv', 'output.xml')