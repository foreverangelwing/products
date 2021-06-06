# 建立記帳程式專案(+二維清單)

products =[]
while True:
	name =input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('輸入商品價格：')
	products.append([name, price])
print(products)



