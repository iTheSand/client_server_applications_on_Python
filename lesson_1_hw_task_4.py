# Задача 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).
enc_str_in_lst = ['разработка', 'администрирование', 'protocol', 'standard']
for enc_str in enc_str_in_lst:
    print(enc_str.encode('utf-8'))

dec_str_bytes_in_lst = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
                        b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5',
                        b'protocol', b'standard']
for dec_str_bytes in dec_str_bytes_in_lst:
    print(dec_str_bytes.decode('utf-8'))
