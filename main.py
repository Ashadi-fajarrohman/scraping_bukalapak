import requests
import csv


key = input('masukan keyword :')
write = csv.writer(open('result/{}.csv'.format(key),'w'))
header = ['nama', 'harga','stok']
write.writerow(header)

url = 'https://api.bukalapak.com/multistrategy-products'
count = 0
for page in range(1, 11):
    parameter = {
    'prambanan_override': True,
    'category_id': 168,
    'keywords': key,
    'limit': 50,
    'offset': 50,
    'page': page,
    'facet': True,
    'access_token': 'FXgMNRgKwTwl5A5pMLDxDJz0CCZmvadOLfudl0FQZtbTzA'
    }

    r = requests.get(url, params=parameter).json()

    products = r['data']
    for p in products:
        nama = p['name']
        harga = p['price']
        stok = p['stock']
        count += 1
        print('nama : ', nama, 'harga :', harga, 'stok :', stok)
        write = csv.writer(open('result/{}.csv'.format(key), 'a'))
        data = [nama, harga, stok]
        write.writerow(data)

