# Dibuat oleh Hanif Abdusy Syakur
# NIM 4.33.23.1.09
# Tugas Jobsheet 13

def guess_number():
    secret_number = 9
    guess = 0
    guess_limit = 3
    
    while guess < guess_limit:
        user = int(input("Masukkan angka > "))
        if user == secret_number:
            print("Selamat, anda berhasil menemukan angkanya")
            break
        else:
            print("Salah!")
            guess += 1
    else:
        print("Anda tidak menemukan angkanya, angka rahasianya adalah {secret_number}")
