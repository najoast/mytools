import os
import sys
import winreg

# 注册 Windows 右键菜单

def gen_command(locale):
	# 获取 python.exe 的绝对路径
	pyUri = sys.executable
	# 获取当前路径，并把当前路径下的 zhconvert.py 转为绝对路径
	curDir = os.path.abspath(os.path.dirname(__file__))
	zhconvertUri = os.path.join(curDir, 'zhconvert.py')
	# 生成命令
	command = r'"%s" "%s" %s "%%1 %%2 %%3 %%4 %%5 %%6 %%7 %%8 %%9"' % (pyUri, zhconvertUri, locale)
	return command

# 写入注册表
# [HKEY_CLASSES_ROOT\*\shell\zhconv_s2t]
# @="简->繁"
# [HKEY_CLASSES_ROOT\*\shell\zhconv_s2t\command]
# @="E:\\dev\\mytools\\zhconv\\zhconv.bat \"%1 %2 %3 %4 %5 %6 %7 %8 %9\""
def register(key, value, locale):
	hkey1 = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r'*\shell', 0, winreg.KEY_ALL_ACCESS) # *\shell
	hkey2 = winreg.CreateKey(hkey1, key) # *\shell\zhconv_s2t
	winreg.SetValueEx(hkey2, '', 0, winreg.REG_SZ, value)
	hkey3 = winreg.CreateKey(hkey2, 'command') # *\shell\zhconv_s2t\command
	# 生成命令
	command = gen_command(locale)
	# 写入注册表
	winreg.SetValueEx(hkey3, '', 0, winreg.REG_SZ, command)
	# 关闭注册表
	winreg.CloseKey(hkey3)
	winreg.CloseKey(hkey2)
	winreg.CloseKey(hkey1)

	print("---------- register ----------\nkey\t%s\nvalue\t%s\ncommand\t%s" % (key, value, command))
	print("registered successfully!\n")

# 删除注册表 [HKEY_CLASSES_ROOT\*\shell\zhconv_s2t]
def unregister(key):
	hkey1 = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r'*\shell', 0, winreg.KEY_ALL_ACCESS)
	# 如果不存在，直接返回
	try:
		hkey2 = winreg.OpenKey(hkey1, key, 0, winreg.KEY_ALL_ACCESS)
		winreg.DeleteKey(hkey2, 'command')
		winreg.DeleteKey(hkey1, key)
		winreg.CloseKey(hkey2)
		winreg.CloseKey(hkey1)
		print('[HKEY_CLASSES_ROOT\*\shell\%s]' % key)
		print("unregistered successfully!\n")
	except:
		print('[HKEY_CLASSES_ROOT\*\shell\%s] not exist!' % key)
		print("unregistered failed!\n")

def bye():
	print("Bye!")
	exit()

# 生成交互式菜单
# 菜单项：注册简体转繁体、注册繁体转简体、删除简体转繁体、删除繁体转简体
def menu():
	print("1. 注册简体转繁体")
	print("2. 注册繁体转简体")
	print("3. 删除简体转繁体")
	print("4. 删除繁体转简体")
	print("5. 退出")
	print("请输入选项：")
	try:
		choice = input()
	except:
		bye()

	if choice == '1':
		register('zhconv_s2t', '简->繁', 'zh-tw')
	elif choice == '2':
		register('zhconv_t2s', '繁->简', 'zh-cn')
	elif choice == '3':
		unregister('zhconv_s2t')
	elif choice == '4':
		unregister('zhconv_t2s')
	elif choice == '5':
		bye()

if __name__ == '__main__':
	while True:
		menu()

