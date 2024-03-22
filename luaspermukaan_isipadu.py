# Atur cara mengira jumlah luas permukaan dan isi padu silinder
# Isytihar pemalar
pi = 3.142

# input
jejari = float(input("Masukkan jejari: "))
tinggi = float(input("Masukkan tinggi: "))

# Proses
jumlah_luas_permukaan= (2 * pi *(jejari**2 )) +(2 * pi * jejari * tinggi)
isipadu= pi * jejari * jejari * tinggi

# Output
print("Jumlah luas permukaan bagi tangki air berbentuk silinder ialah",round(jumlah_luas_permukaan,2),"dan isi padunya ialah ",round(isipadu,2),".")
