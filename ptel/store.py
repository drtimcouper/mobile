
import kivy
kivy.require('1.8.0')

from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore, loads

class PeopStore(object):

    def build(self):
        obj= self.store.get('fred')
        name = obj['name']
        house = obj['house']

        return Label(text='%s @ %s' % (name, house))

    def get_store(self):
        try:
            with open('mydictstore') as f:
                js = f.read()
            return loads(js)
        except IOError:
            pass
        return build_store()

def build_store():
    store = JsonStore('mydictstore')
    store.put('fred', name='Fred Bloggs', house='18 Netherfield Road')
    store.put('john', name='John Smith', house='20 High Street')
    return store


if __name__ == '__main__':
    p = Peops()
    p.run()
