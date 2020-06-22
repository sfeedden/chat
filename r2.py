
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'UTF-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None #一開始預設person是沒有的
	Allen_word_count = 0
	Allen_stick_count = 0
	Allen_pic_count = 0
	Viki_word_count = 0
	Viki_stick_count = 0
	Viki_pic_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				Allen_stick_count += 1
			elif s[2] == '圖片':
				Allen_pic_count += 1
			else:
				for m in s[2]:
					Allen_word_count += len(m)
		if name == 'Viki':
			if s[2] == '貼圖':
				Viki_stick_count += 1
			elif s[2] == '圖片':
				Viki_pic_count += 1
			else:
				for m in s[2]:
					Viki_word_count = len(m)
	print('Allen說了', Allen_word_count , '個字；')
	print('傳了', Allen_stick_count , '張貼圖；')
	print('以及', Allen_pic_count , '張圖片')

	print('Viki說了', Viki_word_count , '個字；')
	print('傳了', Viki_stick_count , '張貼圖；')
	print('以及', Viki_pic_count , '張圖片')


def write_file(filename, lines):
	with open(filename, 'w', encoding= 'UTF-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()
