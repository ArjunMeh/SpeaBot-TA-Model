
from submodel1 import transcribe_streaming
from submodel2 import main
from submodel3 import mark

file_name =  'data.txt'
x = transcribe_streaming('voice1.wav')
print(x)
text_file = open(file_name, "w")
text_file.write(x)
text_file.close()
a = main(file_name)
al = list(dict.fromkeys(a))
for i in al:
    print(i)
mark(file_name)

