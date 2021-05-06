import grammar
import random 

class Tree:
    def __init__(self, data, nodes=[]):
        for node in nodes:
            assert isinstance(node, Tree)
        self.data = data
        self.nodes = nodes
        self.is_expandable = True if nodes else False
    
    def get_nodes(self):
        return self.nodes

    def get_data(self):
        return self.data

    def generate_sentence(self):
        # return a random terminal word
        sentence = ''
        if not self.get_nodes()[0].is_expandable:
            return str(random.choice(self.nodes).get_data()) + ' '
        else:
            for node in self.get_nodes():
                sentence += node.generate_sentence()
            return sentence
