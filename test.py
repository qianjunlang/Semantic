from src.semantic import Analysis

if __name__=='__main__':
	
	text = 'BUPT自然语言处理是谁教的？'

	slu = Analysis(text)
	
	data = slu.analysis()  #解析
	#print(data) #总的结果
	
	#print('--------------------------')
	
	slu.cws #分词
	
	slu.pos #词性标注
		
	print("NER")
	print(slu.ner) #命名实体识别
	
	#print(slu.domain) #领域分类
	
	print("意图识别")
	print(slu.intent) #意图识别
	
	print("槽位填充")
	print(slu.slot) #槽填充
	
	
