print("=================Selamat Datang======================")
#Tampilan1
dict = {'Name': 'Ari', 'Nomor Telepon': 81267888,'Class': 'First'}
dict2 = {'Name': 'Dina', 'Nomor Telepon':87677776,'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Nomor Telepon']: ", dict['Nomor Telepon'])
print ("dict2['Name']: ", dict2['Name'])
print ("dict2['Nomor Telepon']: ", dict2['Nomor Telepon'])

print("=====================================================")

#Tampilan2
dict = {'Name': 'Ari', 'Nomor Telepon': 81267888,'Class': 'First'}
dict2 = {'Name': 'Dina', 'Nomor Telepon':87677776,'Class': 'First'}
dict2['Nomor Telepon'] = 88999776 ; 
dict2['Nama'] = " Dina"
dict3 = {'Name': 'Riko', 'Nomor Telepon': 87654544,'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Nomor Telepon']: ", dict['Nomor Telepon'])
print ("dict2['Nomor Telepon']: ", dict2['Nomor Telepon'])
print ("dict2['Nama']: ", dict2['Nama'])
print ("dict3['Nama']: ", dict3['Name'])
print ("dict3['Nomor Telepon']: ", dict3['Nomor Telepon'])

print("=====================================================")

#Tampilan3
dict = {'Name': 'Dina', 'Nomor Telepon': 87677776 , 'Class': 'First'}
dict2 = {'Name': 'Ari', 'Nomor Telepon': 81267888,'Class': 'First'}
dict3 = {'Name': 'Riko', 'Nomor Telepon': 87654544,'Class': 'First'}


del dict['Name'] 
dict.clear()     
del dict         

print ("dict['Nama']: ", dict['Nama'])
print ("dict['Nomor Telepon']: ", dict['Nomor Telepon'])
print ("dict2['Name']: ", dict2['Name'])
print ("dict2['Nomor Telepon']: ", dict2['Nomor Telepon'])
print ("dict3['Nama']: ", dict3['Name'])
print ("dict3['Nomor Telepon']: ", dict3['Nomor Telepon'])

print("=================Sampai Jumpa Lagi===================")

