import os

def resetfilename():
	print'''
        ����һ�����Ը����ļ�����С����
        �����޸��ļ��ĺ�׺������������ڿ�ת�����ļ�����֮��
        ���� txt -> doc ,�ı����͵�֮���ת���ǿ��Ե�
        �벻Ҫtxt ->xlsx,���������,ǿ���޸Ŀ��ܻᵼ���ļ���,��
	'''	
	path = raw_input('����������Ҫ���ĵ��ļ���·��>>>')
	filename = raw_input('�����뱻�滻����>>>')
	refilename = raw_input('�������滻����>>>')
	try:
		list_dir = os.listdir(path)
		for i in list_dir:
			if filename in i :
				re_i = i.replace(filename,refilename)
				os.rename(os.path.join(path,i),os.path.join(path,re_i))
	except OSError :
		print'������޸ĵ��ļ�����ʹ��״̬,Ϊ�˰�ȫ���,��رձ��滻�ļ���%s���ļ�'%filename

if __name__ == '__main__':
	resetfilename()
