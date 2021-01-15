sentence = ('this is for testing iterables')

def test_itr(sentence):                          #generator, when we use iteration using functions this is generator and when we make whole class and their fucntions it is iteration.
    for word in sentence.split():
        yield word

for test in test_itr(sentence):
    print(test)