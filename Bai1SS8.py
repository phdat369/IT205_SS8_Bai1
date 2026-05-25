# Phân tích 
# Đầu tiên chúng ta cần có 1 menu gồm có 5 chức năng như đề đã yêu cầu 
# Để làm được menu này thì chúng ta cần 1 vòng lặp while với điều kiện là luôn đúng và nó sẽ kết thúc khi người dùng ấn 5 
# Ở chức năng đầu tiên ta cần yêu cầu người dùng nhập vào 4 biến gồm có tên người đăng video, tiêu đề, mô tả, và danh sách hashtag cách nhau bởi dấu phẩy 
# Ở với mỗi video thì chúng ta cần hiển thị như thế này
# - Tên tai khoản sau khi loại bo khoảng trng đau va cuoi
# - Tieu đề sau khi loại bo khoang trang dau va cuoi, viet hoa chu cai dau moi từ
# - Mô tả sau khi loại bỏ khoảng trẳng đầu và cuối
# - Độ dài mô tả video
# - Số lượng từ trong mô tả video
# - Danh sach hashtag sau khi chuan hoa khoảng trang
# - Số lượng hashtag
# - Mô tả video đuoc chuyen toàn bo sang chu thường
# - Mô tả video đưoc chuyen toàn bộ sang chữ hoa
# Ở chức năng thứ 2 thì chúng ta cần chuẩn hóa đúng theo yêu cầu 
# Đầu tiên là tên phải có dấu @ ở đầu 
# Chức năng thứ 3 là kiểm tra hashtag có hợp lên hay không và sau đó in ra thông báo phù hợp với từng loại 
# Chức năng thứ 4 là tìm kiếm theo từ khóa, nếu tồn tại thì thực hiện thay thế bằng từ khóa mới, sau đó hiển thị ra còn nếu không tìm thấy thì in ra thông báo 
# Và cuối cùng là chức năng 5 break ra khỏi vòng lặp và kết thúc chương trình 

# Viết code 

video_description = ""
hashtags = ""
while True:
    print("\n========== MENU ==========")
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên tài khoản TikTok")
    print("3. Kiểm tra hashtag hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả video")
    print("5. Thoát chương trình")
    choose = int(input("Nhập lựa chọn: "))
    match choose:
        case 1:
            username = input("Nhập tên tài khoản: ")
            title = input("Nhập tiêu đề video: ")
            video_description = input("Nhập mô tả video: ")
            hashtags = input("Nhập danh sách hashtag (cách nhau bởi dấu phẩy): ")
            if username.strip() == "":
                print("Tên tài khoản không được rỗng")
                continue
            if video_description.strip() == "":
                print("Mô tả video không được rỗng")
                continue
            username_clean = username.strip()
            title_clean = title.strip().title()
            description_clean = video_description.strip()
            hashtag_list = hashtags.split(",")
            hashtag_clean = []
            for tag in hashtag_list:
                if tag.strip() != "":
                    hashtag_clean.append(tag.strip())
            hashtag_result = ", ".join(hashtag_clean)
            word_count = len(description_clean.split())
            print("\n===== BÁO CÁO THỐNG KÊ =====")
            print(f"Tên tài khoản: {username_clean}")
            print(f"Tiêu đề video: {title_clean}")
            print(f"Mô tả video: {description_clean}")
            print(f"Độ dài mô tả: {len(description_clean)}")
            print(f"Số lượng từ trong mô tả: {word_count}")
            print(f"Danh sách hashtag: {hashtag_result}")
            print(f"Số lượng hashtag: {len(hashtag_clean)}")
            print(f"Mô tả chữ thường: {description_clean.lower()}")
            print(f"Mô tả chữ hoa: {description_clean.upper()}")
        case  2:
            username = input("Nhập tên tài khoản TikTok: ")
            if username.strip() == "":
                print("Tên tài khoản không được rỗng")
                continue
            original_username = username
            username = username.strip().lower()
            if username.startswith("@") == False:
                username = "@" + username
            print(f"Tên tài khoản ban đầu: {original_username}")
            print(f"Tên tài khoản chuẩn hóa: {username}")
        case 3:
            hashtag = input("Nhập hashtag cần kiểm tra: ")
            if hashtag == "":
                print("Hashtag không được rỗng")
            elif hashtag.startswith("#") == False:
                print("Hashtag phải bắt đầu bằng ký tự #")
            elif " " in hashtag:
                print("Hashtag không được chứa khoảng trắng")
            elif len(hashtag) < 2:
                print("Hashtag phải có ít nhất 2 ký tự")
            else:
                valid = True
                for char in hashtag[1:]:
                    if not (char.isalnum() or char == "_"):
                        valid = False
                        break
                if valid:
                    print("Hashtag hợp lệ")
                    if hashtags == "":
                        hashtags = hashtag
                    else:
                        hashtags = hashtags + ", " + hashtag
                    print(f"Danh sách hashtag hiện tại: {hashtags}")
                else:
                    print("Hashtag chỉ được chứa chữ cái, số hoặc dấu gạch dưới")
        case 4:
            if video_description.strip() == "":
                print("Chưa có mô tả video để tìm kiếm")
                continue
            find_keyword = input("Nhập từ khóa cần tìm: ")
            replace_keyword = input("Nhập từ khóa thay thế: ")
            description_clean = video_description.strip()
            if find_keyword in description_clean:
                count_keyword = description_clean.count(find_keyword)
                new_description = description_clean.replace(find_keyword, replace_keyword)
                print("Mô tả sau khi thay thế:")
                print(new_description)
                print(f"Số lần xuất hiện: {count_keyword}")
                video_description = new_description
            else:
                print("Không tìm thấy từ khóa trong mô tả video")
        case 5:
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ")