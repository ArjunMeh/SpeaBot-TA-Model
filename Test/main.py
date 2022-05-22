
from submodel1 import transcribe_streaming
from submodel2 import main
from submodel3 import mark

file_name =  'data.txt'
x = transcribe_streaming('woman1_wb.wav')
print(x)
text_file = open(file_name, "w")
text_file.write(x)

a = main('test.txt')
al = list(dict.fromkeys(a))
print(al)
marks =  mark(file_name)

