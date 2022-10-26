"""
MTG class to interface with api as well as save pickle files
also working on a basic deck builder to pull cards from set by a certain type

TODO: method showCardInfo (variable len)
"""


from mtgsdk import Card, Set
import pickle


class MagicK:
    def __init__(self):
        self.cardObj = Card
        self.setObj = Set
        #self.cardObj

    @staticmethod
    def get_sets(self):
        # todo: remove: dont need this any more
        set_data = {}
        for setObj in sets:
            # todo: pack in csv so i can see the shit! :)
            print(setObj.name, ", ", setObj.code)
            set_data[setObj.name] = setObj.code

        print(set_data)

    @staticmethod
    def open_pickle_file():
        pickle_file = open(filename, 'rb')
        objects = pickle.load(filename)

    def print_card_data(self, card_object, full=0):
        """
        print out cards data from its object
        :param card_object MTG card object with populated data
        :param full: whether to show the description
        :return:
        """
        #card_object = self.cardObj
        print(card_object.colors, card_object.name, card_object.type, card_object.image_url)

    @staticmethod
    def load_pickle_file_into_object(filename):
        objects = []
        with (open('Pickles/'+filename + '.pkl', "rb")) as openfile:
            while True:
                try:
                    objects.append(pickle.load(openfile))
                except EOFError:
                    break

        return objects

    def get_cards_by_type(self, filename, color='Blue', card_type='Creature'):
        """
        list all cards in set by type and color
        :param filename:
        :param card_type:
        :param color:
        :return: could return object
        todo: could sort as well. this is a great feature. 
        """

        set_obj = self.load_pickle_file_into_object(filename)
        for item in set_obj[0]:
            # debug
            #print(item.type.find(card_type))
            # 2 do: maybe another way to break this down.
            if item.type.find(card_type) > -1:
                """ check for single color and match"""
                if len(item.colors) == 1 and item.colors[0] == color:
                    self.print_card_data(item)
            # debug: print all
            else:
                # this would need to only flag once, etc.
                # debug
                print("card type not found printing item")
                self.print_card_data(item)


    @staticmethod
    def pickle_this(name, data):
        # todo: make a method
        pickle_file = open('Pickles/'+name+'.pkl', 'wb')
        pickle.dump(data, pickle_file)
        pickle_file.close()

    def get_all_cards_in_set(self, set_name='AKH', proper_name='file_name'):
        """
        get all cards in set via the api and pickle them locally!
        :param set_name:
        :param proper_name:
        :return:
        """
        print("getting cards")
        set = self.cardObj.where(set=set_name).all()
        print("got all the cards")
        self.pickle_this(proper_name, set)
        print("pickle file of set created!")


mk = MagicK()

#mk.get_all_cards_in_set('Legions', 'LGN')

# set (pickle) name, color (def blue), type (def creature)
#mk.get_cards_by_type('Amonket', 'Creature')
mk.get_cards_by_type('Dragons_Tarkir', 'Blue', 'Elemental')
