def tinh_tong_so(list):
    tong = 0
    for num in list:
        if num % 2 == 0:
            tong += num 
    return tong
# Nhập danh sách từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách các s, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

# Sử dụng hàm và inkeets quả
tong_chan = tinh_tong_so(numbers)
print("Tống các số chẵn trong list là:", tong_chan)