
"""
................................................. Subarray Division ....................................................

LINK ORIGIN: https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true

Hai đứa trẻ, Lily và Ron, muốn chia sẻ một thanh sô cô la. Mỗi ô vuông có một số nguyên trên đó.
Lily quyết định chia sẻ một phân đoạn liền kề của thanh sô cô la được chọn sao cho:
    - Độ dài của phân đoạn khớp với tháng sinh của Ron và,
    - Tổng các số nguyên trên các ô vuông bằng ngày sinh của anh ấy.
Xác định xem cô ấy có thể chia sô cô la bằng bao nhiêu cách.

VÍ DỤ:
    s = [2, 2, 1, 3, 2]
    d = 4
    m = 2
    Lily muốn tìm các phân đoạn tính đến ngày sinh của Ron,d = 4 có độ dài bằng với tháng sinh của anh ấy ,. Trong trường hợp này, m = 2  có hai phân đoạn đáp ứng tiêu chí của cô ấy:[2, 2] và[1, 3].

MÔ TẢ:
    Hoàn thành chức năng sinh nhật trong trình chỉnh sửa bên dưới.
Ngày sinh có (các) tham số sau:
    - int s [n]: số trên mỗi ô vuông sô cô la
    - int d: Ngày sinh của Ron
    - int m: Tháng sinh của Ron

KẾT QUẢ TRẢ VỀ:
    - int: số cách thanh có thể được chia

ĐỊNH DẠNG CỦA INPUT:
    - Dòng đầu tiên chứa một số nguyên n, số ô vuông trong thanh sô cô la.
    - Dòng thứ hai là các phần tử của mảng chứa các số in trên từng ô vuông.
    - Dòng thứ ba chứa hai số nguyên được phân tách bằng dấu cách, ngày sinh của Ron và tháng sinh của anh ấy.

RÀNG BUỘC:
    1 <= n <= 100
    1 <= s[i] <= 5, where (0 <= i <= n)
    1 <= d <= 31
    1 <= m <= 12
............................................ EXAMPLE 0 .............................................
INPUT MẪU 0:
    5
    1 2 1 3 2
    3 2
OUTPUT MẪU 0:
    2
GIẢI THÍCH MẪU 0:
    Lily muốn đưa cho Ron m=2 hình vuông tính tổng các ô vuông của Ron d = 3. Hai phân đoạn sau đáp ứng các tiêu chí:

hình ảnh.....
............................................ EXAMPLE 0 .............................................

INPUT MẪU 1:
    6
    1 1 1 1 1 1
    3 2
OUTPUT MẪU 1:
    0
GIẢI THÍCH MẪU 1:
    Lily chỉ muốn cho Ron m = 2 những hình vuông sô cô la liên tiếp có tổng các số nguyên d = 3. Không có phần nào có thể đáp ứng các ràng buộc này:

hình ảnh ..........

Vì vậy, chúng tôi in như câu trả lời của chúng tôi.

Đầu vào mẫu 2
    1
    4
    4 1
Đầu ra mẫu 2
    1
Giải thích 2
Lily chỉ muốn cho Ron m = 1 hình vuông sô cô la có giá trị nguyên là d = 4. Bởi vì hình vuông sô cô la duy nhất trong thanh thỏa mãn hạn chế này, vì thế câu trả lời là 1.
"""


# Complete the birthday function below.
def birthday(s, d, m):
    numOfWays = 0

    for i in range(len(s)):
        lenOfTheSeg = s[i:m + i]
        if sum(lenOfTheSeg) == d: numOfWays += 1

    return numOfWays


if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')
