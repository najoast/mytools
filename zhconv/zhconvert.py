

# 转入一个文件，把文件中的简体中文转为繁体中文
# 入参：locale, inputFile, outputFile（如果不填, 在输入文件名后加上 _zh-cn/tw, 后缀不变）

import os
import sys
import codecs
from zhconv import convert

def zhConvert(locale, inputUri, outputUri):
	print('converting ' + inputUri + ' to ' + outputUri)
	inputFile = codecs.open(inputUri, 'r', 'utf-8')
	outputFile = codecs.open(outputUri, 'w', 'utf-8')
	for line in inputFile:
		outputFile.write(convert(line, locale))
	inputFile.close()
	outputFile.close()

def main():
	locale = sys.argv[1]
	inputFile = sys.argv[2]
	outputFile = None
	if len(sys.argv) > 3:
		outputFile = sys.argv[3]
	if not os.path.exists(inputFile):
		print('file not exists: ' + inputFile)
		exit()
	
	if not outputFile:
		# 取出 inputFile 的前缀和后缀
		prefix, suffix = os.path.splitext(inputFile)
		outputFile = prefix + "_" + locale + suffix

	outputDir = os.path.dirname(outputFile)
	if outputDir and not os.path.exists(outputDir):
		os.makedirs(os.path.dirname(outputFile))
	
	zhConvert(locale, inputFile, outputFile)

if __name__ == '__main__':
	main()