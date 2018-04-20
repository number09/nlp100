import xml.etree.ElementTree as ET
import pydot
import graphviz

def main():

    tree = ET.parse('nlp.txt.xml')

    root = tree.getroot()

    document = root[0][1]

    for sentence in document.iter('sentence'):
        zyutugo_dict = {}
        for keydep in sentence.iterfind(
            'dependencies[@type="collapsed-dependencies"]/dep[@type="nsubj"]'
        ):
            dep = keydep.find('dependent')
            syugo = dep.text
            gov = keydep.find('governor')
            if gov is not None:
                zyutugo = gov.text

                if zyutugo_dict.get(zyutugo, None) is None:
                    zyutugo_dict[zyutugo] = {}
                zyutugo_dict[zyutugo]['syugo'] = syugo

        for keydep in sentence.iterfind(
                'dependencies[@type="collapsed-dependencies"]/dep[@type="dobj"]'
        ):
            dep = keydep.find('dependent')
            mokutekigo = dep.text
            gov = keydep.find('governor')
            if gov is not None:
                zyutugo = gov.text

                if zyutugo_dict.get(zyutugo, None) is None:
                    zyutugo_dict[zyutugo] = {}
                zyutugo_dict[zyutugo]['mokutekigo'] = mokutekigo

        #print(zyutugo_dict)

        #todo : あっているか再確認

        for zyu, val in zyutugo_dict.items():
            if 'syugo' in val.keys() and 'mokutekigo' in val.keys():
                print(val['syugo'], zyu, val['mokutekigo'])






if __name__ == '__main__':
    main()
