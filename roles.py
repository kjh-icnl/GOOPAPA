from google_trans_new import google_translator, constant


def translate(TXT, src='Auto', dst='Auto'):
	translator = google_translator()
	count = 0
	src_key = ''
	dst_key = ''

	if dst == 'Auto':
		dst = 'English'
		dst_key = 'en'

	if src == 'Auto':
		src_key, src = detect(translator, TXT)
		
		for key, value in constant.LANGUAGES.items():
			if value == dst.lower():
				dst_key = key
				break

	else:
		for key, value in constant.LANGUAGES.items():
			if count >= 2:
				break
			elif value == src.lower():
				src_key = key
				count += 1

			elif value == dst.lower():
				dst_key = key
				count += 1
			else:
				continue

	
	if src_key == '' or dst_key == '':
		return "ERROR", None, None

	if src == dst:
		return txt, src.capitalize(), src.capitalize()
	else:
		txts = TXT.split('\n')

		TXT = '' #initailization
		for txt in txts:
			translated = translator.translate(txt, lang_src = src_key, lang_tgt = dst_key)
			TXT += (translated +'\n') 
			
		return TXT, src.capitalize(), dst.capitalize()


def detect(translator, TXT):
	detected = translator.detect(TXT)
	return detected[0], detected[1]
	#return key, value