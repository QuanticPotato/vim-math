import vim
buffer = None
characters = []
lines = []
currentSlot = None

def init():
	global buffer
	global characters
	characters = []
	lines = []
	buffer = vim.current.buffer
	newLine()


def newLine():
	global currentSlot
	global lines
	currentSlot = Slot(True)
	lines.append(currentSlot)


def updateStringOnScreen(position, string):
	x = position.x
	y = position.y
	while len(characters) - 1 < y:
		buffer.append('')
		characters.append([])

	while len(characters[y]) - 1 < x:
		characters[y].append(' ')

	for i in range(len(string)):
		characters[y][x + i] = string[i]

	buffer[y] = ''.join(characters[y])


def processKey():
	key = vim.bindeval('g:math_key')
	if isASCIIKey(key) or True:
		currentSlot.appendASCII(key)


def isASCIIKey(key):
	""" The ASCII code (for the printable characters) range over 32 to 126 (in decimal) """
	return key >= 32 or key <= 126


class Coords:
	x = 0
	y = 0

	def __init__(self, _x, _y):
		self.x = _x
		self.y = _y

	def addPoint(self, point):
		return Coords(self.x + point.x, self.y + point.y)

	def add(self, x, y):
		self.x += x
		self.y += y
		return self


class Slot:
	topslot = False
	elements = []
	currentElement = 0
	position = Coords(0, 0)
	cursor = Coords(0, 0)

	def __init__(self, isTopslot):
		self.topslot = isTopslot
		self.elements.append(String())

	def appendASCII(self, code):
		element = self.elements[self.currentElement]
		if isinstance(element, String):
			element.value += chr(code)
		else:
			self.currentElement = String(chr(code))
			self.elements.append(self.currentElement)
			element = self.currentElement
		updateStringOnScreen(self.position.addPoint(self.cursor), [chr(code)])
		self.cursor.add(1, 0)


class String:
	value = ''
