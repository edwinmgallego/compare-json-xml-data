import json
import xml.etree.ElementTree as ET

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def ver_pila(self):
        return self.items

def recorrer_json(data, pila, prefix=''):
    if isinstance(data, dict):
        for key, value in data.items():
            new_prefix = f"{prefix}.{key}" if prefix else key
            recorrer_json(value, pila, new_prefix)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            new_prefix = f"{prefix}[{index}]"
            recorrer_json(item, pila, new_prefix)
    else:
        pila.apilar((prefix, data))

def recorrer_xml(elemento, pila, prefix=''):
    for child in elemento:
        new_prefix = f"{prefix}.{child.tag}" if prefix else child.tag
        if child.text and child.text.strip():
            pila.apilar((new_prefix, child.text.strip()))
        recorrer_xml(child, pila, new_prefix)
        for key, value in child.attrib.items():
            attrib_prefix = f"{new_prefix}@{key}"
            pila.apilar((attrib_prefix, value))
            


def main():
    # Procesar archivo JSON
    nombre_archivo_json = 'nuevo1json/nuevo1.json'  # Reemplaza con el nombre de tu archivo JSON
    with open(nombre_archivo_json, 'r') as archivo_json:
        datos_json = json.load(archivo_json)

    pila_json = Pila()
   
    recorrer_json(datos_json, pila_json)

    # Procesar archivo XML
    nombre_archivo_xml = 'nuevo1xml/xmkOk.xml'  # Reemplaza con el nombre de tu archivo XML
    tree = ET.parse(nombre_archivo_xml)
    root = tree.getroot()

    pila_xml = Pila() 
    recorrer_xml(root, pila_xml)

    # Comparar valores de ambas pilas
    valores_json = {item[1] for item in pila_json.ver_pila()}
    valores_xml = {item[1] for item in pila_xml.ver_pila()}

    coincidencias = valores_json.intersection(valores_xml)

    # Imprimir coincidencias
    if coincidencias:
        print("Coincidencias encontradas:")
        for valor in coincidencias:
            print(valor)
    else:
        print("No se encontraron coincidencias.")

if __name__ == "__main__":
    main()
