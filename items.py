import json, random, io
from random_words import RandomWords

array = []
words = RandomWords()

for n in range(0, 100000):
	data = {}
	data['title'] = ' '.join(words.random_words(count=random.randint(1,6)))
	data['description'] = ' '.join(words.random_words(count=random.randint(4,60)))
	integers = [random.randint(200,800+1) for x in range(2)]
	strings = [''.join([random.choice('0123456789ABCDEF') for x in range(6)]) for y in range(2)]
	data['image'] = "http://dummyimage.com/%dx%d/%s/%s" % (integers[0], integers[1], strings[0], strings[1])
	array.append(data)

open('items.json', 'w').write(json.dumps(array))