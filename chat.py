
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'UTF-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None #一開始預設person是沒有的
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person是有值的
			new.append(person + ': ' + line)
	print(new)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding= 'UTF-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()
