dict2= {'Name': 'Ari', 'Nomor Telepon': 81267888}
dict5= {'Name': 'Dina', 'Nomor Telepon':87677776}   
dict3= {'Name': 'Riko', 'Nomor Telepon': 87654544}

data=[]
while(True):
   print ("=========Daftar Kontak=============")
   print ( dict5 ['Name'],dict5 ['Nomor Telepon'])
   print ( dict2['Name'],dict2['Nomor Telepon'])
   print ( dict3['Name'],dict3['Nomor Telepon'])
   ulangi=input("LANJUTKAN (t)?")
   if ulangi .lower()== 't' :
       break
print("\nSAMPAI JUMPA LAGI TERIMA KASIH\n")
dict4= {'Name': 'Ari', 'Nomor Telepon':81267888}
dict5= {'Name': 'Dina', 'Nomor Telepon':87677776}
dict5['Nomor Telepon'] = 88999776  
dict5['Nama'] = " Dina"
dict6= {'Name': 'Riko', 'Nomor Telepon': 87654544}
print ("=========Daftar Kontak=============")
print ( dict4 ['Name'],dict4['Nomor Telepon'])
print ( dict5['Name'],dict5['Nomor Telepon'])
print ( dict6['Name'],dict6['Nomor Telepon'])

dict4= {'Name': 'Ari', 'Nomor Telepon':81267888}
dict= {'Name': 'Dina', 'Nomor Telepon':87677776}
dict6= {'Name': 'Riko', 'Nomor Telepon': 87654544}
del dict['Name'] 
dict.clear()     
del dict         

print ("=========Daftar Kontak=============")
print ( dict4 ['Name'],dict4['Nomor Telepon'])
print ( dict['Name'],dict['Nomor Telepon'])
print ( dict6['Name'],dict6['Nomor Telepon'])

