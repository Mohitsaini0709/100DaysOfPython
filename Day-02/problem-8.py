name = input("Entre Your Name : ")

letter = '''
Dear <|Name|>,
You are Selected!
<|Date|>
'''
print(letter.replace("<|Name|>",name ).replace("<|Date|>","5/4/2026"))
