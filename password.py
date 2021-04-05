password = 'a123456'
chance = 3 # 最多3次輸入機會
while chance > 0:
	chance = chance - 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break # 逃出迴圈
	else:
		print('密碼錯誤!')
		if chance > 0:
			print('還有', chance, '次機會')
		else:
			print('沒有機會嘗試了! 要鎖帳號了啦!')

