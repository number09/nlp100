import xml.etree.ElementTree as ET
import pydot
import graphviz

def main():

    tree = ET.parse('nlp.txt.xml')

    root = tree.getroot()

    document = root[0][1]

    for sentence in document.iter('sentence'):
        kakari_tree = []
        for dep in sentence.iterfind(
            'dependencies[@type="collapsed-dependencies"]/dep'
        ):
            gov = dep.find('governor')
            dep = dep.find('dependent')

            kakari_tree.append(
                (gov.text, dep.text)
            )


        #g = pydot.graph_from_edges(kakari_tree)

        g = graphviz.Digraph(format='jpg')
        g.edges(kakari_tree)
        g.render('kakari_tree')


if __name__ == '__main__':
    main()
