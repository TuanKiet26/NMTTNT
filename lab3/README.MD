# Bài Tập 1: Thuật toán di truyền cho bài toán tối ưu hóa
Mục tiêu: Sử dụng thuật toán di truyền để tối ưu hóa hàm mục tiêu 
h(x)=sin(x)+cos(x) trong khoảng x∈[0,2π].
Thuật toán di truyền hoạt động dựa trên cơ chế chọn lọc tự nhiên và tiến hóa, bao gồm các bước chính như sau:
1. Khởi tạo quần thể (initialize_population)
Mô tả: Đầu tiên, quần thể ban đầu được khởi tạo ngẫu nhiên. Mỗi cá thể trong quần thể là một giá trị x ngẫu nhiên trong khoảng [0,2π].
Cách hoạt động: Dùng np.random.uniform(min_val, max_val) để tạo ra một giá trị ngẫu nhiên cho mỗi cá thể trong quần thể.
2. Hàm mục tiêu (fitness_function_1d)
Mô tả: Hàm mục tiêu sẽ tính giá trị fitness của mỗi cá thể. Trong bài toán này, giá trị fitness được tính là h(x)=sin(x)+cos(x).
Cách hoạt động: Hàm này sẽ trả về giá trị h(x) cho mỗi cá thể x trong quần thể.
3. Lựa chọn cha mẹ (select_parents)
Mô tả: Cơ chế lựa chọn cha mẹ trong thuật toán di truyền sử dụng phương pháp Tournament Selection. Trong phương pháp này, một số cá thể được chọn ngẫu nhiên và sau đó cá thể có giá trị fitness cao nhất được chọn làm cha mẹ.
4. Lai ghép (crossover)
Mô tả: Sau khi chọn được cha mẹ, chúng ta thực hiện lai ghép để tạo ra con cái. Cơ chế lai ghép là kết hợp hai cha mẹ để tạo ra con cái mới.
Cách hoạt động: Với xác suất crossover (mặc định là 80%), con cái sẽ là trung bình của hai cha mẹ, nếu không thì nó sẽ là một bản sao của một trong các cha mẹ.
5. Đột biến (mutation)
Mô tả: Sau khi lai ghép, con cái sẽ có khả năng bị đột biến để tạo ra sự đa dạng trong quần thể. Đột biến thay đổi giá trị của cá thể con cái một cách ngẫu nhiên.
Cách hoạt động: Với xác suất mutation (mặc định là 10%), giá trị của cá thể con sẽ bị thay đổi ngẫu nhiên trong khoảng [0,2π].
6. Thuật toán di truyền chính (genetic_algorithm_1d)
Mô tả: Đây là hàm chính điều khiển toàn bộ quá trình di truyền. Nó thực hiện các bước như khởi tạo quần thể, tính toán fitness, chọn cha mẹ, lai ghép, đột biến và tạo ra các thế hệ tiếp theo cho đến khi hoàn thành số thế hệ mong muốn.
Cách hoạt động:
Quần thể được khởi tạo ngẫu nhiên.
Mỗi thế hệ, fitness của các cá thể được tính toán.
Các cá thể tốt nhất được chọn làm cha mẹ và lai ghép để tạo ra quần thể mới.
Lặp lại quá trình này cho đến khi đạt số thế hệ mong muốn.
Cuối cùng, cá thể có giá trị fitness tốt nhất được chọn làm kết quả tối ưu.
# Bài Tập 2: Vẽ đồ thị tiến hóa
Mục tiêu: Vẽ đồ thị tiến hóa của giá trị fitness qua các thế hệ.
Sau khi thuật toán di truyền hoàn thành, bạn có thể theo dõi sự thay đổi của giá trị fitness tốt nhất qua các thế hệ bằng cách vẽ đồ thị.
1. Vẽ đồ thị:
Mô tả: Dùng thư viện matplotlib để vẽ đồ thị của quá trình tiến hóa. Đồ thị này sẽ hiển thị giá trị fitness tốt nhất ở mỗi thế hệ.
Cách hoạt động: Sau khi thuật toán di truyền hoàn thành, ta dùng plt.plot(history) để vẽ giá trị fitness tốt nhất qua các thế hệ.
Tóm tắt quy trình hoạt động:
Khởi tạo quần thể: Tạo quần thể ban đầu với các giá trị ngẫu nhiên.
Tính fitness: Đánh giá mỗi cá thể trong quần thể bằng hàm mục tiêu.
Lựa chọn cha mẹ: Chọn các cha mẹ bằng phương pháp Tournament Selection.
Lai ghép và đột biến: Lai ghép và đột biến tạo ra con cái cho thế hệ mới.
Lặp lại: Tiếp tục quá trình cho đến khi đủ số thế hệ.
Vẽ đồ thị tiến hóa: Theo dõi sự tiến hóa của giá trị fitness qua các thế hệ.
Mục tiêu cuối cùng của thuật toán là tìm giá trị h(x)=sin(x)+cos(x) gần với giá trị tối ưu lý thuyết.
# Bài tập 3 : Thay đổi tham số thuật toán di truyền và phân tích tốc độ hội tụ 
1. Mục tiêu
Thuật toán này được thiết kế để tìm giá trị f(x,y)=sin(x)+cos(y) đạt giá trị lớn nhất.
2. Khởi tạo quần thể
Đầu tiên, chương trình tạo ra một tập hợp các cá thể (được gọi là quần thể) với kích thước pop_size (ví dụ 30 cá thể).  Mỗi cá thể là một cặp số thực (x,y), được chọn ngẫu nhiên trong khoảng giá trị xác định (ví dụ từ -5 đến 5).
Đây chính là các "điểm khởi đầu" để thuật toán bắt đầu tìm kiếm.
3. Tính giá trị fitness
Với mỗi cá thể, thuật toán tính giá trị của hàm mục tiêu f(x,y) (tức fitness).
Giá trị fitness phản ánh “độ tốt” của cá thể đó — tức là độ gần đúng hoặc chất lượng của nghiệm đó.
4. Chọn lọc cha mẹ (Selection)
Thuật toán chọn ra các cá thể tốt nhất làm cha mẹ để sinh ra thế hệ mới.
Cách chọn là Tournament Selection:
Ngẫu nhiên chọn vài cá thể trong quần thể (ví dụ 3 cá thể).
Trong nhóm đó, chọn cá thể có fitness cao nhất làm cha mẹ.
Điều này đảm bảo những cá thể tốt có cơ hội truyền gen nhiều hơn.
5. Lai ghép (Crossover)
Cha mẹ được lai ghép để tạo ra con cái.
Với xác suất (ví dụ 80%), con cái được tạo bằng cách lấy trung bình cộng từng thành phần x và  y của cha mẹ.
Nếu không lai ghép, con cái giữ nguyên gen của cha mẹ.
Lai ghép giúp kết hợp đặc điểm tốt của các cha mẹ, tạo ra các con mới có thể tốt hơn.
6. Đột biến (Mutation)
Để tránh bị kẹt ở những điểm không tối ưu, thuật toán áp dụng đột biến.
Với xác suất nhỏ (ví dụ 10%), giá trị x hoặc y của con cái bị thay thế bằng một giá trị ngẫu nhiên mới trong phạm vi cho phép.
Đột biến giúp duy trì đa dạng di truyền trong quần thể.
7. Cập nhật quần thể
Sau khi sinh ra đủ số cá thể cho thế hệ mới, quần thể được cập nhật bằng các con cái mới.
Quá trình tính fitness, chọn lọc, lai ghép và đột biến được lặp lại cho đến khi đạt đủ số thế hệ (ví dụ 50 thế hệ).
8. Theo dõi kết quả
Ở mỗi thế hệ, chương trình ghi lại giá trị fitness cao nhất và in ra cá thể tốt nhất.
Cuối cùng, thuật toán trả về cá thể có fitness cao nhất qua tất cả các thế hệ.
9. Hiển thị kết quả
Cuối cùng, thuật toán vẽ biểu đồ quá trình tiến hóa giá trị fitness tốt nhất qua từng thế hệ.
# Bài Tập 4 : Cải thiện  thuật toán thêm  phương pháp lựa chọn khác và so sánh hiệu quả
Mục tiêu
Tối ưu hàm f(x,y)=sin(x)+cos(y) bằng thuật toán di truyền.
(x,y) sao cho giá trị hàm mục tiêu lớn nhất.
Các bước chính:
1. Khởi tạo quần thể
Tạo pop_size cá thể, mỗi cá thể là một cặp (x,y) ngẫu nhiên trong khoảng [min_val,max_val].
2. Tính fitness
Tính giá trị hàm mục tiêu cho từng cá thể, dùng làm fitness.
3. Chọn lọc cha mẹ
Có 3 phương pháp chọn lọc được hỗ trợ:
random: chọn cha mẹ ngẫu nhiên.
roulette: chọn theo xác suất tỉ lệ với fitness (cá thể có fitness cao có xác suất được chọn cao hơn).
tournament: chọn ra nhóm ngẫu nhiên rồi lấy cá thể tốt nhất trong nhóm làm cha mẹ.
Bạn có thể dễ dàng thay đổi phương pháp chọn lọc khi gọi thuật toán.
4. Lai ghép
Với xác suất crossover_rate, con được tạo bằng cách lấy trung bình của cha mẹ.
Nếu không, con giữ gen cha mẹ 1.
5. Đột biến
Với xác suất mutation_rate, mỗi biến 
x hoặc y có thể bị thay đổi ngẫu nhiên.
6. Cập nhật thế hệ
Sinh ra quần thể mới bằng cách lặp lại quá trình chọn lọc, lai ghép, đột biến cho đến đủ số lượng cá thể.
7. Theo dõi và in kết quả
Sau mỗi thế hệ, in ra cá thể tốt nhất và giá trị fitness tương ứng.
Lưu lại lịch sử giá trị fitness tốt nhất qua các thế hệ.
8. Vẽ biểu đồ
Vẽ đồ thị biểu diễn sự thay đổi của giá trị fitness tốt nhất qua các thế hệ, giúp quan sát tiến trình tối ưu.
Kết quả
Thuật toán sẽ trả về cá thể có giá trị fitness tốt nhất sau số thế hệ đã định.
Bạn có thể so sánh hiệu quả của các phương pháp chọn lọc khác nhau bằng cách chạy lần lượt các phương pháp random, roulette, tournament
# Bài tập 5 : Trực quan hóa quần thể
Mục tiêu bài toán:
Tối thiểu hóa hàm 
g(x,y)=x2 +y2
  → điểm cực tiểu là (0,0) với giá trị nhỏ nhất là 0.
Vì thuật toán di truyền chỉ tìm cực đại, ta đảo dấu hàm mục tiêu thành 
f(x,y)=−x2−y2.
 6.Các bước hoạt động chính:
Bước 1: Khởi tạo quần thể
python
Copy
Edit
initialize_population_2d()
Tạo ngẫu nhiên pop_size cá thể, mỗi cá thể là một cặp (x,y) trong khoảng [−5,5].
Bước 2: Tính fitness
Tính fitness bằng hàm f(x,y)=−x2−y2
Giá trị càng lớn (tức càng gần 0), cá thể càng tốt.
Bước 3: Chọn cha mẹ
Chọn ngẫu nhiên một nhóm nhỏ (3 cá thể) từ quần thể, sau đó chọn cá thể tốt nhất trong nhóm làm cha mẹ.
Cách chọn này giúp tăng khả năng chọn cá thể tốt mà vẫn giữ được sự ngẫu nhiên.
Bước 4: Lai ghép 
Với xác suất 80%, tạo cá thể con bằng cách lấy trung bình tọa độ của cha và mẹ.
Nếu không lai, giữ nguyên một trong hai cha mẹ.
Bước 5: Đột biến
Với xác suất 10%, x hoặc y (hoặc cả hai) bị thay đổi ngẫu nhiên trong khoảng [-5, 5].
Đột biến giúp duy trì tính đa dạng, tránh bị kẹt ở cực trị cục bộ.
Bước 6: Sinh thế hệ mới
Lặp lại quá trình chọn → lai → đột biến để tạo quần thể mới cho thế hệ tiếp theo.
Quá trình lặp lại trong generations thế hệ.
Bước 7: Lưu và vẽ quần thể
Sau mỗi thế hệ, quần thể được lưu để sau đó vẽ biểu đồ.
Vẽ biểu đồ phân tán (scatter plot) của các cá thể theo từng thế hệ để quan sát sự hội tụ về điểm tối ưu (gần gốc tọa độ).
Kết quả kỳ vọng
Sau nhiều thế hệ, các cá thể sẽ dần tụ lại gần điểm (0, 0).
Trên đồ thị, bạn sẽ thấy các điểm phân tán ban đầu rộng, rồi tập trung dần vào giữa, thể hiện quá trình tìm cực tiểu.