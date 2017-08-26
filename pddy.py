import os

def resetfilename():
	print'''
        这是一个可以更改文件名的小程序
        可以修改文件的后缀名，但是请介于可转换的文件类型之间
        例如 txt -> doc ,文本类型的之间的转换是可以的
        请不要txt ->xlsx,臣妾做不到,强制修改可能会导致文件损坏,亲
	'''	
	path = raw_input('请输入你需要更改的文件夹路径>>>')
	filename = raw_input('请输入被替换的字>>>')
	refilename = raw_input('请输入替换的字>>>')
	try:
		list_dir = os.listdir(path)
		for i in list_dir:
			if filename in i :
				re_i = i.replace(filename,refilename)
				os.rename(os.path.join(path,i),os.path.join(path,re_i))
	except OSError :
		print'请别让修改的文件处于使用状态,为了安全起见,请关闭被替换文件带%s的文件'%filename

if __name__ == '__main__':
	resetfilename()
