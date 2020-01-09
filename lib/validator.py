import logging
import wordninja

class Validator():
    """
    Description: This class is used to split string and identify if blacklisted word is in the string 
    :params: data: "thisisalongstrong"
    :return Dict containing: {'message': 'Success', 'output': 'this is a long string', 'blaclisted': ['long']}
    """
    def __init__(self, data: str = None):
        self.input_data = data
        self.parsed_data = None
        self.wordsplit = None
        self.wordsplit_file = 'dev/words_library.txt.gz'
        self.blacklisted = []
        self.blacklisted_list = None
        self.blaclisted_file = 'dev/blacklist_strings.txt'
        self.result = {
            'message': 'Error',
            'output': self.parsed_data,
            'blaclisted': self.blacklisted
        }

    def init_blacklist_word(self):
        """ Load the blacklist words from a file """
        try:
            with open(self.blaclisted_file, 'r') as file:
                self.blacklisted_list = file.read().splitlines()
        except Exception as e:
            raise Exception(e)

    def init_word_library(self):
        """ Init the word library for splitting """
        try:
            self.wordsplit = wordninja.LanguageModel(self.wordsplit_file)
        except Exception as e:
            raise Exception(e)

    def split_string(self):
        """ Split input string """
        try:
            self.parsed_data = self.wordsplit.split(self.input_data)
        except Exception as e:
            raise Exception("Error Split String: %s " % e)

    def check_blacklisted(self):
        """ Check blacklisted string """
        try:
            for words in self.parsed_data:
                if words in self.blacklisted_list:
                    self.blacklisted.append(words)
        except Exception as e:
            raise Exception("Error checking blacklist %s" % e)

    def run(self):
        """ Entrypoint of this class """
        if self.input_data is None:
            logging.error("No input string provided")
            return self.result
        try:
            self.init_blacklist_word()
            self.init_word_library()
            self.split_string()
            self.check_blacklisted()
        except Exception as e:
            logging.error(e)
        else:
            self.result['message'] = 'Success'
            self.result['output'] = ' '.join(self.parsed_data)
            self.result['blaclisted'] = self.blacklisted
        finally:
            return self.result

# if __name__ == '__main__':
#     v = StringValidator('Lovesbeer').run()
#     print(v)