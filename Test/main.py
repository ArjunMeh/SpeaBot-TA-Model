
from submodel1 import transcribe_streaming
from submodel2 import main
x = transcribe_streaming('woman1_wb.wav')
print(x)
text_file = open("data.txt", "w")
text_file.write(x)
file_name =  'data.txt'
a = main('test.txt')
al = list(dict.fromkeys(a))
print(al)