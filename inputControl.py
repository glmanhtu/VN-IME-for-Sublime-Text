import sublime, sublime_plugin
class InputcontrolCommand(sublime_plugin.TextCommand):
	curPost = 0
	state = True
	curSize = 0
	curEdit = 0
	keyDefine = ['w','s','f','x','j','a','o','e','d','r','z']
	def run(self, edit):
		self.curSize = self.view.size();
		self.curEdit = edit;
		sublime.set_timeout_async(self.run_in_background, 0)
	def run_in_background(self):
		pos = self.view.sel()[0]
		if self.view.size() > self.curSize :
			a = pos.begin() - 1
			b = pos.end()
			charRegion = sublime.Region(a, b)
			char = self.view.substr(charRegion)
			if self.find_key_unicode(char):
				final = self.replace_word_key(char,self.view.word(charRegion))
				if final :
					self.view.run_command("runchange", {'a':a,'b':b,"final":final})
					print(charRegion)
			self.curPost = pos                 
			self.curSize = self.view.size();
		elif self.view.size() < self.curSize:
			self.curSize = self.view.size();
		if self.state == True:
			sublime.set_timeout_async(self.run_in_background, 100)
	def find_key_unicode(self,key):
		if key in self.keyDefine: 
			return True
		return False  
	def replace_word_key(self,key,word):
		word = self.view.substr(word)
		finalWord = '' 
		charSour = ''
		charDest = ''
		if key == 'w':
			charSour = ['a','o','u']
			charDest = ['ă','ơ','ư']
		elif key == 's':
			charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư']
			charDest = ['á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ']
		elif key == 'f':
			charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư','ì']
			charDest = ['à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ','if']
		elif key ==	'x':
			charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư','ẽ']
			charDest = ['ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ','ex']
		elif key ==	'j':
			charSour = ['a','ă','â','e','ê','i','o','ơ','ô','u','ư']
			charDest = ['ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ụ','ự']
		elif key ==	'a':
			charSour = ['a','ă','â']
			charDest = ['â','â','aa']
		elif key ==	'o':
			charSour = ['o','ơ','ô']
			charDest = ['ô','ô','oo']
		elif key ==	'e':
			charSour = ['e','ê']
			charDest = ['ê','ee']	
		elif key ==	'd':
			charSour = ['d','đ']
			charDest = ['đ','dd']	
		elif key ==	'r':
			charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư']
			charDest = ['ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử']
		finalWord = self.convertWordChar(key,word,charSour,charDest)
		if finalWord != word:	
			return finalWord
		return False
	def convertWordChar(self,key,word,charSour,charDest):
		w = list(word)
		hasChanged = False
		del w[len(word)-1]
		for i in range(len(w)):
			if hasChanged:
				break
			for j in range(len(charSour)):
				if w[i] == charSour[j]:
					w[i] = charDest[j]
					hasChanged = True
					break
		if hasChanged :
			word = "".join(w) 
		return word


class RunchangeCommand(sublime_plugin.TextCommand):
	def run(self, edit, a, b, final):
		charRegion = sublime.Region(a, b)
		self.view.replace(edit,self.view.word(charRegion),final)