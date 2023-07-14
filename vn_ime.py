import sublime, sublime_plugin

STATUS = False
MOD = False 
LASTKEY = ''
class SaveOnModifiedListener(sublime_plugin.EventListener):
    def on_modified(self, view):
    	global STATUS
    	global MOD
    	if not STATUS:
    		return
    	if not MOD:
    		view.run_command('startime')
    	MOD = False
class StartimeCommand(sublime_plugin.TextCommand): 
	curPost = 0
	curSize = 0
	stateIME = True
	keyDefine = ['w','s','f','x','j','a','o','e','d','r','z']
	def run(self, edit):
		pos = self.view.sel()[0] 
		global LASTKEY
		if self.view.size() > self.curSize : 
			a = pos.begin() - 1
			b = pos.end()	
			charRegion = sublime.Region(a, b)
			char = self.view.substr(charRegion).lower()
			if self.find_key_unicode(char):
				if self.check_grammar(self.view.word(charRegion)):
					final = self.replace_word_key(char,self.view.word(charRegion))
					if final :
						global MOD
						self.view.run_command("runchange", {'a':a,'b':b,"final":final})  
						MOD = True
			self.curPost = pos                 
			self.curSize = self.view.size();
			LASTKEY = char
		elif self.view.size() < self.curSize:
			self.curSize = self.view.size();
		
	def find_key_unicode(self,key):
		if key in self.keyDefine: 
			return True
		return False  
	def check_grammar(self,word):
		word = self.view.substr(word)	
		# _len = len(word)-2
		# for i in _len:
		# 	if word[i] == word[i+1]: 
		# 		return False
		return True 

	def replace_word_key(self,key,word):
		word = self.view.substr(word)
		finalWord = '' 
		charSour = ''
		charDest = ''
		if key == 'w':
			charSour = ['a','o','u','ă','ơ','ư','â','A','O','U','Ă','Ơ','Ư','Â']
			charDest = ['ă','ơ','ư','a','o','u','a','Ă','Ơ','Ư','A','O','U','A']
		elif key == 's':
			charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư','á','í','é','ó','ý','ú','A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư','Á','Í','É','Ó','Ý','Ú']
			charDest = ['á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ','a','i','e','o','y','u','Á','Ắ','Ấ','É','Ế','Í','Ó','Ớ','Ố','Ý','Ú','Ứ','A','I','E','O','Y','U']
		elif key == 'f':
			charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư','ì','à','è','ì','ò','ỳ','A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư','Ì','À','È','Ì','Ò','Ỳ']
			charDest = ['à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ','i','a','e','i','o','y','À','Ằ','Ầ','È','Ề','Ì','Ò','Ờ','Ồ','Ỳ','Ù','Ừ','I','A','E','I','O','Y']
		elif key ==	'x':
			charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư','ẽ','ã','ẽ','ĩ','õ','ỹ','ũ','A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư','Ẽ','Ã','Ẽ','Ĩ','Õ','Ỹ','Ũ']
			charDest = ['ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ','e','a','e','i','o','y','u','Ã','Ẵ','Ẫ','Ẽ','Ễ','Ĩ','Õ','Ỡ','Ỗ','Ỹ','Ũ','Ữ','E','A','E','I','O','Y','U']
		elif key ==	'j':
			charSour = ['a','ă','â','e','ê','i','o','ơ','ô','u','ư','ạ','ẹ','ị','ọ','ụ','A','Ă','Â','E','Ê','I','O','Ơ','Ô','U','Ư','Ạ','Ẹ','Ị','Ọ','Ụ']
			charDest = ['ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ụ','ự','a','e','i','o','u','Ạ','Ặ','Ậ','Ẹ','Ệ','Ị','Ọ','Ợ','Ộ','Ụ','Ự','A','E','I','O','U']
		elif key ==	'a':
			charSour = ['a','ă','â','A','Ă','Â']
			charDest = ['â','â','a','Â','Â','A']
		elif key ==	'o':
			charSour = ['o','ơ','ô','O','Ơ','Ô']
			charDest = ['ô','ô','o','Ô','Ô','O']
		elif key ==	'e':
			charSour = ['e','ê','E','Ê']
			charDest = ['ê','e','Ê','E']
		elif key ==	'd':
			charSour = ['d','đ','D','Đ']
			charDest = ['đ','d','Đ','D']	
		elif key ==	'r':
			charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư','ỏ','ả','ẻ','ỉ','ỏ','ỷ','ủ','A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư','Ỏ','Ả','Ẻ','Ỉ','Ỏ','Ỷ','Ủ']
			charDest = ['ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử','o','a','e','i','o','y','u','Ả','Ẳ','Ẩ','Ẻ','Ể','Ỉ','Ỏ','Ở','Ổ','Ỷ','Ủ','Ử','O','A','E','I','O','Y','U']
		finalWord = self.convertWordChar(key,word,charSour,charDest)
		if finalWord != word:	
			return finalWord
		return False
	def convertWordChar(self,key,word,charSour,charDest):
		global LASTKEY
		w = list(word)
		hasChanged = False
		del w[-1]

		if len(w) >6 or (len(w) >2 and w[0] in ['o','e', 'O', 'E'] ):
			return word
		if len(w) > 3 or (len(w)==3 and w[2] in ['o', 'O']) :
			for i in reversed(range(len(w))):
				if hasChanged:
					break
				for j in range(len(charSour)):
					if (i in [3,4] and w[i] in ['i','u', 'I', 'U']):
						continue
					if (w[i] == charSour[j]) : 
						w[i] = charDest[j]	
						hasChanged = True
						break		
		elif len(w) <= 3:				
			for i in range(len(w)):
				if hasChanged:
					break
				for j in range(len(charSour)):
					if w[i] == charSour[j]:
						w[i] = charDest[j]
						hasChanged = True
						break
		if LASTKEY == key:
			if w[-1] == key:
				w.append(LASTKEY)
		if hasChanged :
			word = "".join(w) 
		return word
class ControlimeCommand(sublime_plugin.TextCommand):
	stateIME = True
	def run(self, edit):
		global STATUS
		if self.stateIME == False:
			STATUS = False
			self.stateIME = True 		
			sublime.status_message("VN IME Stoped")
			self.view.set_status('VN IME'," VN IME : OFF")
		elif self.stateIME :
			STATUS = True	
			self.stateIME = False
			sublime.status_message("VN IME Started")
			self.view.set_status('VN IME'," VN IME : ON")

class RunchangeCommand(sublime_plugin.TextCommand):
	def run(self, edit, a, b, final):
		charRegion = sublime.Region(a, b)
		self.view.replace(edit,self.view.word(charRegion),final)
