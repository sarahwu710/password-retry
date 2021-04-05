password = 'a123456'
chance = 3 # 最多3次輸入機會
while chance > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break # 逃出迴圈
	else:
		chance = chance - 1
		print('密碼錯誤! 還有', chance, '次機會')

