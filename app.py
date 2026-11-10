import streamlit as st
import random, time
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="PINK | Kinh tế chính trị", page_icon="🌸", layout="wide", initial_sidebar_state="expanded")

st.markdown('''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
html,body,[class*="css"]{font-family:'Poppins',sans-serif!important} .stApp{background:linear-gradient(135deg,#fff8fc 0%,#fff 48%,#fff2f8 100%);color:#44313e}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#fff0f7,#f9e9f5);border-right:1px solid #f4d5e7}
.hero{padding:30px 34px;border-radius:26px;background:linear-gradient(120deg,#f8c9df,#ead8fa 58%,#fff0f7);box-shadow:0 12px 35px #d9a9c533;position:relative;overflow:hidden}
.hero:after{content:'✿';position:absolute;right:35px;top:-28px;font-size:150px;color:#ffffff77;animation:float 5s ease-in-out infinite}
@keyframes float{0%,100%{transform:translateY(0) rotate(-8deg)}50%{transform:translateY(14px) rotate(8deg)}}
.card{background:#fff;border:1px solid #f4dce9;border-radius:20px;padding:20px 22px;box-shadow:0 8px 25px #d8a9c51c;margin-bottom:12px}
.kicker{color:#bd6f9a;font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase}.big{font-size:28px;font-weight:800;color:#8d4c75}.muted{color:#967f8e;font-size:13px}
.pill{display:inline-block;background:#fff0f7;color:#a64e7d;padding:5px 11px;border-radius:30px;font-size:12px;font-weight:600;margin:3px}
.stButton>button{border-radius:12px;border:1px solid #e9b9d2;background:linear-gradient(110deg,#f7c8df,#ead8fa);color:#673b57;font-weight:600;transition:.2s}.stButton>button:hover{transform:translateY(-2px);box-shadow:0 7px 18px #d8a9c555;border-color:#d993b8}
div[data-testid="stProgressBar"]>div>div{background:linear-gradient(90deg,#e99bc2,#b89be8)}
.stRadio label{font-size:14px}.stExpander{border:1px solid #f1d7e6!important;border-radius:14px!important;background:#fff}
hr{border-color:#f3dce9!important}
</style>''', unsafe_allow_html=True)

# The study guide follows the six-chapter structure of the supplied Mác-Lênin political-economy materials.
CHAPTERS = [
{"title":"Đối tượng, phương pháp và chức năng","short":"Nền tảng môn học","intro":"Hiểu kinh tế chính trị nghiên cứu điều gì, bằng cách nào và để làm gì.","sections":[
("Khái quát sự hình thành","Thuật ngữ khoa học kinh tế chính trị xuất hiện ở châu Âu năm 1615 trong tác phẩm Chuyên luận về kinh tế chính trị. Quá trình phát triển có thể khái quát thành hai thời kỳ: từ cổ đại đến thế kỷ XVIII và từ sau thế kỷ XVIII đến nay. Chủ nghĩa trọng thương đề cao thương mại, nhất là ngoại thương; chủ nghĩa trọng nông nhấn mạnh sản xuất nông nghiệp. Kinh tế chính trị cổ điển Anh gắn với William Petty, Adam Smith và David Ricardo."),
("Khái niệm và đối tượng nghiên cứu","Kinh tế chính trị nghiên cứu các quan hệ kinh tế để tìm ra những quy luật chi phối sự vận động của các hiện tượng và quá trình hoạt động kinh tế của con người, tương ứng với trình độ phát triển nhất định của nền sản xuất xã hội. Trọng tâm là quan hệ sản xuất trong mối liên hệ với lực lượng sản xuất và kiến trúc thượng tầng."),
("Phương pháp nghiên cứu","Phương pháp luận cơ bản là phép biện chứng duy vật. Trừu tượng hóa khoa học là phương pháp chủ yếu, quan trọng nhất: gạt bỏ những yếu tố ngẫu nhiên, không bản chất để nhận ra mối liên hệ bản chất, ổn định. Ngoài ra còn có logic kết hợp lịch sử, thống kê, so sánh, phân tích - tổng hợp, quy nạp - diễn dịch, hệ thống hóa, mô hình hóa và tổng kết thực tiễn."),
("Bốn chức năng","Nhận thức: phát hiện bản chất và quy luật kinh tế. Thực tiễn: cung cấp luận cứ khoa học cho hoạch định đường lối, chính sách và biện pháp kinh tế. Tư tưởng: góp phần hình thành thế giới quan, nhân sinh quan. Phương pháp luận: cung cấp nền tảng lý luận cho các khoa học kinh tế chuyên ngành, chức năng và một số khoa học khác.")],
"facts":[("Đối tượng nghiên cứu của kinh tế chính trị","Các quan hệ kinh tế và quy luật chi phối sự vận động của chúng"),("Thuật ngữ kinh tế chính trị xuất hiện năm nào?","Năm 1615 tại châu Âu"),("Tác phẩm gắn với lần xuất hiện thuật ngữ","Chuyên luận về kinh tế chính trị"),("Chủ nghĩa trọng thương đề cao điều gì?","Thương mại, đặc biệt là ngoại thương"),("Chủ nghĩa trọng nông nhấn mạnh điều gì?","Vai trò của sản xuất nông nghiệp"),("Các đại biểu kinh tế chính trị cổ điển Anh","William Petty, Adam Smith, David Ricardo"),("Phương pháp luận cơ bản","Phép biện chứng duy vật"),("Phương pháp chủ yếu, quan trọng nhất","Trừu tượng hóa khoa học"),("Trừu tượng hóa khoa học nhằm mục đích gì?","Gạt yếu tố ngẫu nhiên để nhận thức bản chất và mối liên hệ tất yếu"),("Chức năng nhận thức","Phát hiện bản chất hiện tượng, quá trình và quy luật kinh tế"),("Chức năng thực tiễn","Cung cấp luận cứ khoa học để hoạch định chính sách và biện pháp kinh tế"),("Chức năng tư tưởng","Góp phần hình thành thế giới quan và nhân sinh quan"),("Chức năng phương pháp luận","Làm nền tảng lý luận cho các khoa học kinh tế"),("Kinh tế chính trị cổ điển Anh phát triển mạnh vào giai đoạn nào?","Cuối thế kỷ XVIII đến nửa đầu thế kỷ XIX"),("Kinh tế chính trị Mác - Lênin ra đời vào thời kỳ nào?","Giữa thế kỷ XIX"),("Kinh tế chính trị Mác - Lênin kế thừa trực tiếp trường phái nào?","Kinh tế chính trị cổ điển Anh"),("Tác phẩm thể hiện tập trung lý luận của Mác","Bộ Tư bản"),("Logic kết hợp lịch sử là gì?","Xem xét sự vật theo trình tự lịch sử và khái quát logic bản chất"),("Phân tích - tổng hợp","Tách các mặt để nghiên cứu rồi liên kết thành nhận thức chỉnh thể"),("Quy nạp","Từ những trường hợp riêng rút ra kết luận chung"),("Diễn dịch","Từ nguyên lý chung suy ra trường hợp cụ thể"),("Thống kê và so sánh có tác dụng gì?","Thu thập, đối chiếu dữ liệu để nhận ra đặc điểm và xu hướng"),("Kinh tế chính trị nghiên cứu quan hệ kinh tế trong bối cảnh nào?","Tương ứng với trình độ phát triển nhất định của nền sản xuất xã hội"),("Chức năng thực tiễn có quan hệ thế nào với nhận thức?","Dựa trên kết quả nhận thức bản chất và quy luật kinh tế"),("Vì sao kinh tế chính trị có chức năng phương pháp luận?","Vì phạm trù và quy luật chung là cơ sở lý luận cho các ngành khoa học kinh tế") ]},
{"title":"Hàng hóa, thị trường và vai trò của các chủ thể","short":"Hàng hóa & thị trường","intro":"Nắm chắc hàng hóa, hai thuộc tính, lượng giá trị, tiền tệ và quy luật giá trị.","sections":[
("Sản xuất hàng hóa","Sản xuất hàng hóa là kiểu tổ chức kinh tế mà sản phẩm được sản xuất ra để trao đổi, mua bán trên thị trường. Hai điều kiện ra đời: phân công lao động xã hội và sự tách biệt tương đối về kinh tế giữa những người sản xuất do các hình thức sở hữu tư liệu sản xuất quy định."),
("Hàng hóa và hai thuộc tính","Hàng hóa là sản phẩm của lao động, có thể thỏa mãn nhu cầu nào đó của con người thông qua trao đổi, mua bán. Hàng hóa có hai thuộc tính: giá trị sử dụng và giá trị. Giá trị sử dụng là công dụng; giá trị là lao động xã hội của người sản xuất hàng hóa kết tinh trong hàng hóa."),
("Lượng giá trị hàng hóa","Lượng giá trị được đo bằng thời gian lao động xã hội cần thiết. Năng suất lao động tăng làm lượng giá trị một đơn vị hàng hóa giảm; cường độ lao động tăng làm tổng giá trị tạo ra trong một đơn vị thời gian tăng, còn giá trị một đơn vị hàng hóa không đổi nếu các điều kiện khác không đổi."),
("Tiền tệ và thị trường","Tiền tệ là hàng hóa đặc biệt đóng vai trò vật ngang giá chung. Các chức năng cơ bản gồm thước đo giá trị, phương tiện lưu thông, phương tiện cất trữ, phương tiện thanh toán và tiền tệ thế giới. Thị trường là tổng hòa các quan hệ kinh tế trong đó nhu cầu của các chủ thể được đáp ứng thông qua trao đổi, mua bán."),
("Quy luật giá trị","Sản xuất và trao đổi hàng hóa phải dựa trên hao phí lao động xã hội cần thiết. Trong sản xuất, quy luật điều tiết phân bổ nguồn lực; trong lưu thông, trao đổi theo nguyên tắc ngang giá; đồng thời kích thích cải tiến kỹ thuật, hợp lý hóa sản xuất và phân hóa người sản xuất.")],
"facts":[("Sản xuất hàng hóa","Kiểu tổ chức kinh tế mà sản phẩm được sản xuất ra để trao đổi, mua bán"),("Điều kiện thứ nhất của sản xuất hàng hóa","Phân công lao động xã hội"),("Điều kiện thứ hai của sản xuất hàng hóa","Sự tách biệt tương đối về kinh tế giữa những người sản xuất"),("Hàng hóa","Sản phẩm của lao động có thể thỏa mãn nhu cầu thông qua trao đổi, mua bán"),("Hai thuộc tính của hàng hóa","Giá trị sử dụng và giá trị"),("Giá trị sử dụng","Công dụng của hàng hóa trong thỏa mãn nhu cầu"),("Giá trị hàng hóa","Lao động xã hội của người sản xuất kết tinh trong hàng hóa"),("Thước đo lượng giá trị hàng hóa","Thời gian lao động xã hội cần thiết"),("Năng suất lao động tăng thì giá trị một đơn vị hàng hóa","Giảm xuống"),("Cường độ lao động tăng làm tổng giá trị trong cùng thời gian","Tăng lên"),("Tiền tệ","Hàng hóa đặc biệt đóng vai trò vật ngang giá chung"),("Chức năng thước đo giá trị","Biểu hiện và đo lường giá trị hàng hóa bằng tiền"),("Chức năng phương tiện lưu thông","Làm môi giới trong trao đổi hàng hóa"),("Chức năng phương tiện cất trữ","Rút tiền khỏi lưu thông để tích lũy"),("Chức năng phương tiện thanh toán","Dùng tiền để trả nợ, trả tiền hàng mua chịu và nghĩa vụ"),("Thị trường","Tổng hòa các quan hệ kinh tế thông qua trao đổi, mua bán"),("Quy luật giá trị yêu cầu sản xuất dựa trên","Hao phí lao động xã hội cần thiết"),("Quy luật giá trị trong lưu thông yêu cầu","Trao đổi theo nguyên tắc ngang giá"),("Vai trò điều tiết của quy luật giá trị","Điều tiết sản xuất và lưu thông hàng hóa"),("Vai trò kích thích của quy luật giá trị","Thúc đẩy cải tiến kỹ thuật, tăng năng suất và hợp lý hóa sản xuất"),("Hệ quả phân hóa của quy luật giá trị","Người sản xuất có điều kiện khác nhau có thể phân hóa giàu nghèo"),("Lao động cụ thể tạo ra","Giá trị sử dụng"),("Lao động trừu tượng tạo ra","Giá trị hàng hóa"),("Hai mặt của lao động sản xuất hàng hóa","Lao động cụ thể và lao động trừu tượng"),("Khi năng suất lao động tăng, giá trị mới tạo ra trong một giờ","Không đổi nếu cường độ và thời gian lao động không đổi") ]},
{"title":"Giá trị thặng dư trong nền kinh tế thị trường","short":"Giá trị thặng dư","intro":"Đây là chương trọng tâm: sức lao động, tư bản bất biến/khả biến, m và các phương pháp sản xuất giá trị thặng dư.","sections":[
("Công thức chung của tư bản","Tiền chỉ trở thành tư bản khi vận động theo công thức T - H - T’, trong đó T’ = T + ΔT. Phần tăng thêm ΔT là giá trị thặng dư. Mục đích của lưu thông tư bản là giá trị tăng thêm, khác với lưu thông hàng hóa giản đơn H - T - H."),
("Hàng hóa sức lao động","Sức lao động trở thành hàng hóa khi người lao động được tự do về thân thể và không có đủ tư liệu sản xuất để tự mình kết hợp với tư liệu sản xuất tạo ra sản phẩm. Giá trị hàng hóa sức lao động do giá trị tư liệu sinh hoạt cần thiết để tái sản xuất sức lao động quyết định; giá trị sử dụng đặc biệt là tạo ra giá trị mới lớn hơn giá trị bản thân nó."),
("Tư bản bất biến và tư bản khả biến","Tư bản bất biến (c) là bộ phận tư bản tồn tại dưới hình thái tư liệu sản xuất, giá trị được bảo toàn và chuyển vào sản phẩm. Tư bản khả biến (v) là bộ phận tư bản dùng mua sức lao động, thông qua lao động sống tạo ra giá trị mới và giá trị thặng dư."),
("Giá trị thặng dư và tỷ suất","Giá trị thặng dư (m) là phần giá trị mới dôi ra ngoài giá trị sức lao động do công nhân làm thuê tạo ra và bị nhà tư bản chiếm đoạt. Tỷ suất giá trị thặng dư m’ = (m/v) × 100%, phản ánh trình độ bóc lột sức lao động."),
("Các phương pháp sản xuất giá trị thặng dư","Tuyệt đối: kéo dài ngày lao động khi thời gian lao động tất yếu không đổi. Tương đối: rút ngắn thời gian lao động tất yếu nhờ tăng năng suất lao động xã hội. Siêu ngạch: giá trị thặng dư thu được do giá trị cá biệt thấp hơn giá trị xã hội.")],
"facts":[("Công thức chung của tư bản","T - H - T’"),("T’ trong công thức tư bản","Giá trị tiền ứng trước cộng với giá trị tăng thêm"),("Mục đích vận động của tư bản","Giá trị tăng thêm"),("Điều kiện để sức lao động trở thành hàng hóa","Người lao động tự do thân thể và không có đủ tư liệu sản xuất"),("Giá trị hàng hóa sức lao động do yếu tố nào quyết định?","Giá trị tư liệu sinh hoạt cần thiết để tái sản xuất sức lao động"),("Giá trị sử dụng đặc biệt của hàng hóa sức lao động","Tạo ra giá trị mới lớn hơn giá trị bản thân nó"),("Tư bản bất biến ký hiệu","c"),("Tư bản khả biến ký hiệu","v"),("Tư bản bất biến","Bộ phận tư bản đầu tư vào tư liệu sản xuất, giá trị chuyển vào sản phẩm"),("Tư bản khả biến","Bộ phận tư bản đầu tư mua sức lao động"),("Giá trị thặng dư ký hiệu","m"),("Giá trị thặng dư","Phần giá trị mới dôi ra ngoài giá trị sức lao động do lao động làm thuê tạo ra"),("Tỷ suất giá trị thặng dư","m’ = (m/v) × 100%"),("Tỷ suất giá trị thặng dư phản ánh","Trình độ bóc lột sức lao động"),("Phương pháp sản xuất giá trị thặng dư tuyệt đối","Kéo dài ngày lao động khi thời gian lao động tất yếu không đổi"),("Phương pháp sản xuất giá trị thặng dư tương đối","Rút ngắn thời gian lao động tất yếu"),("Giá trị thặng dư siêu ngạch","Phần giá trị thặng dư do giá trị cá biệt thấp hơn giá trị xã hội"),("Ngày lao động gồm","Thời gian lao động tất yếu và thời gian lao động thặng dư"),("Thời gian lao động tất yếu","Thời gian người lao động tạo ra giá trị ngang với giá trị sức lao động"),("Thời gian lao động thặng dư","Thời gian tạo ra giá trị thặng dư"),("Tích lũy tư bản","Chuyển hóa một phần giá trị thặng dư thành tư bản phụ thêm"),("Nguồn gốc của tích lũy tư bản","Giá trị thặng dư"),("Cấu tạo hữu cơ của tư bản","Cấu tạo giá trị do cấu tạo kỹ thuật quyết định và phản ánh sự biến đổi của cấu tạo kỹ thuật"),("Tuần hoàn của tư bản","Sự vận động của tư bản qua các giai đoạn và hình thái, thực hiện các chức năng tương ứng"),("Chu chuyển tư bản","Tuần hoàn tư bản xét như quá trình định kỳ, lặp đi lặp lại") ]},
{"title":"Cạnh tranh và độc quyền trong nền kinh tế thị trường","short":"Cạnh tranh & độc quyền","intro":"Hiểu cạnh tranh, độc quyền, độc quyền nhà nước và tác động trong chủ nghĩa tư bản.","sections":[
("Cạnh tranh","Cạnh tranh là sự ganh đua giữa các chủ thể kinh tế nhằm giành những điều kiện thuận lợi trong sản xuất, tiêu thụ hàng hóa và thu lợi ích kinh tế. Cạnh tranh thúc đẩy đổi mới, nâng cao năng suất nhưng cũng có thể dẫn đến phân hóa và các hành vi cạnh tranh không lành mạnh."),
("Độc quyền","Độc quyền hình thành khi tích tụ, tập trung sản xuất và sự liên kết giữa các doanh nghiệp đạt đến mức độ nhất định, tạo ra các tổ chức độc quyền chi phối một bộ phận hoặc toàn bộ thị trường. Độc quyền có thể tác động thúc đẩy tiến bộ kỹ thuật, nhưng cũng có thể hạn chế cạnh tranh, áp đặt giá cả và phân phối lại lợi ích."),
("Quan hệ giữa cạnh tranh và độc quyền","Độc quyền không xóa bỏ cạnh tranh. Cạnh tranh vẫn tồn tại giữa các tổ chức độc quyền, giữa tổ chức độc quyền với doanh nghiệp ngoài độc quyền và giữa các doanh nghiệp ngoài độc quyền."),
("Tư bản tài chính và xuất khẩu tư bản","Sự dung hợp giữa tư bản ngân hàng và tư bản công nghiệp tạo ra tư bản tài chính. Xuất khẩu tư bản là đưa tư bản ra nước ngoài để kinh doanh nhằm thu giá trị thặng dư và các lợi ích khác."),
("Độc quyền nhà nước","Độc quyền nhà nước trong chủ nghĩa tư bản là sự kết hợp sức mạnh của các tổ chức độc quyền tư nhân với nhà nước tư sản, nhằm phục vụ lợi ích của tư bản độc quyền và thích ứng với những điều kiện phát triển mới.")],
"facts":[("Cạnh tranh","Sự ganh đua giữa các chủ thể kinh tế để giành điều kiện thuận lợi và lợi ích"),("Mục tiêu trực tiếp của cạnh tranh","Giành điều kiện thuận lợi trong sản xuất, tiêu thụ và thu lợi ích kinh tế"),("Một tác động tích cực của cạnh tranh","Thúc đẩy đổi mới kỹ thuật và nâng cao năng suất"),("Một tác động tiêu cực có thể có của cạnh tranh","Phân hóa chủ thể và phát sinh cạnh tranh không lành mạnh"),("Độc quyền","Sự chi phối thị trường của tổ chức/doanh nghiệp có vị thế độc quyền"),("Nguồn gốc kinh tế chủ yếu của độc quyền","Tích tụ, tập trung sản xuất và liên kết doanh nghiệp"),("Độc quyền có xóa bỏ cạnh tranh không?","Không, cạnh tranh vẫn tồn tại dưới nhiều hình thức"),("Cạnh tranh giữa các tổ chức độc quyền","Vẫn tồn tại để giành thị trường, nguồn lực và lợi ích"),("Cạnh tranh giữa độc quyền và doanh nghiệp ngoài độc quyền","Vẫn tồn tại"),("Tư bản tài chính","Sự dung hợp giữa tư bản ngân hàng và tư bản công nghiệp"),("Xuất khẩu tư bản","Đưa tư bản ra nước ngoài để kinh doanh, thu lợi ích"),("Xuất khẩu hàng hóa khác xuất khẩu tư bản ở điểm nào?","Xuất khẩu tư bản đưa giá trị ra nước ngoài để đầu tư sinh lời"),("Độc quyền nhà nước tư bản chủ nghĩa","Sự kết hợp sức mạnh tổ chức độc quyền tư nhân với nhà nước tư sản"),("Mục đích của độc quyền nhà nước","Phục vụ lợi ích của tư bản độc quyền và điều tiết nền kinh tế theo lợi ích đó"),("Tích tụ tư bản","Tăng quy mô tư bản cá biệt bằng tích lũy"),("Tập trung tư bản","Tăng quy mô tư bản cá biệt bằng hợp nhất hoặc sáp nhập các tư bản có sẵn"),("Khác biệt tích tụ và tập trung tư bản","Tích tụ dựa vào tích lũy; tập trung dựa vào hợp nhất tư bản có sẵn"),("Giá độc quyền","Giá cả do tổ chức độc quyền chi phối nhằm thu lợi nhuận độc quyền"),("Lợi nhuận độc quyền","Lợi nhuận cao hơn mức lợi nhuận bình quân do vị thế độc quyền tạo điều kiện"),("Cạnh tranh trong nội bộ ngành","Cạnh tranh giữa các doanh nghiệp cùng ngành"),("Cạnh tranh giữa các ngành","Cạnh tranh giữa các ngành để tìm nơi đầu tư có lợi hơn"),("Vai trò của nhà nước tư sản trong độc quyền nhà nước","Can thiệp, điều tiết và hỗ trợ các điều kiện hoạt động của tư bản độc quyền"),("Độc quyền có thể thúc đẩy điều gì?","Nghiên cứu, ứng dụng tiến bộ kỹ thuật khi có lợi ích kinh tế"),("Độc quyền có thể gây ra điều gì?","Hạn chế cạnh tranh và áp đặt điều kiện thị trường"),("Cạnh tranh là quy luật kinh tế của","Nền sản xuất và trao đổi hàng hóa") ]},
{"title":"Kinh tế thị trường định hướng xã hội chủ nghĩa ở Việt Nam","short":"Kinh tế Việt Nam","intro":"Nắm đặc trưng, thể chế, các thành phần kinh tế và quan hệ lợi ích kinh tế.","sections":[
("Kinh tế thị trường định hướng XHCN","Là nền kinh tế vận hành đầy đủ, đồng bộ theo các quy luật của kinh tế thị trường, đồng thời bảo đảm định hướng xã hội chủ nghĩa phù hợp từng giai đoạn phát triển của đất nước. Mục tiêu hướng tới phát triển lực lượng sản xuất, xây dựng cơ sở vật chất - kỹ thuật, nâng cao đời sống nhân dân và thực hiện dân giàu, nước mạnh, dân chủ, công bằng, văn minh."),
("Năm đặc trưng trong tài liệu tóm tắt","Gồm: mục tiêu phát triển; quan hệ sở hữu và thành phần kinh tế; quan hệ quản lý; quan hệ phân phối; gắn tăng trưởng kinh tế với công bằng xã hội."),
("Sở hữu và thành phần kinh tế","Theo tài liệu tóm tắt, kinh tế nhà nước giữ vai trò chủ đạo, kinh tế tư nhân là một động lực quan trọng. Các thành phần kinh tế bình đẳng trước pháp luật, hợp tác và cạnh tranh theo pháp luật."),
("Quản lý và phân phối","Nhà nước quản lý bằng pháp luật, chiến lược, kế hoạch, quy hoạch, cơ chế, chính sách và công cụ kinh tế, trên cơ sở tôn trọng nguyên tắc thị trường. Các hình thức phân phối được nêu gồm theo kết quả lao động, theo hiệu quả kinh tế và theo phúc lợi."),
("Quan hệ lợi ích kinh tế","Lợi ích kinh tế là lợi ích vật chất thu được khi thực hiện các hoạt động kinh tế. Quan hệ lợi ích có thể thống nhất hoặc mâu thuẫn; cần hài hòa lợi ích, kiểm soát quan hệ tiêu cực và giải quyết mâu thuẫn.")],
"facts":[("Mục tiêu của kinh tế thị trường định hướng XHCN","Phát triển lực lượng sản xuất, nâng cao đời sống nhân dân và hướng tới dân giàu, nước mạnh, dân chủ, công bằng, văn minh"),("Kinh tế nhà nước giữ vai trò gì?","Vai trò chủ đạo"),("Kinh tế tư nhân được xác định là gì?","Một động lực quan trọng"),("Nhà nước quản lý nền kinh tế bằng","Pháp luật, chiến lược, kế hoạch, quy hoạch, cơ chế, chính sách và công cụ kinh tế"),("Quản lý nhà nước phải dựa trên cơ sở nào?","Tôn trọng các nguyên tắc của thị trường và định hướng mục tiêu phát triển"),("Các hình thức phân phối trong tài liệu tóm tắt","Theo kết quả lao động, hiệu quả kinh tế và phúc lợi"),("Phân phối theo kết quả lao động dựa trên","Số lượng và chất lượng lao động"),("Phân phối theo hiệu quả kinh tế dựa trên","Lãi, lỗ và lợi tức"),("Phân phối theo phúc lợi","Thông qua các chính sách phúc lợi xã hội"),("Đặc trưng về tăng trưởng và công bằng","Gắn tăng trưởng kinh tế với công bằng xã hội"),("Kinh tế thị trường định hướng XHCN vận hành theo","Các quy luật của kinh tế thị trường"),("Định hướng XHCN thể hiện qua","Mục tiêu, sở hữu, quản lý, phân phối và công bằng xã hội"),("Thể chế kinh tế","Hệ thống quy tắc, luật pháp, bộ máy quản lý và cơ chế vận hành nền kinh tế"),("Hoàn thiện thể chế sở hữu cần chú trọng","Quyền sở hữu, quyền tài sản và sở hữu trí tuệ"),("Hoàn thiện thể chế doanh nghiệp cần","Chế độ pháp lý kinh doanh nhất quán, pháp luật đầu tư và cạnh tranh"),("Phát triển đồng bộ các yếu tố thị trường","Hoàn thiện thể chế để các yếu tố và loại thị trường vận hành thông suốt"),("Lợi ích kinh tế","Lợi ích vật chất thu được khi thực hiện hoạt động kinh tế"),("Quan hệ lợi ích kinh tế","Mối quan hệ giữa các chủ thể trong quá trình thực hiện lợi ích kinh tế"),("Quan hệ lợi ích có thể ở trạng thái nào?","Thống nhất hoặc mâu thuẫn"),("Nguyên tắc xử lý quan hệ lợi ích","Hài hòa lợi ích, kiểm soát tác động tiêu cực và giải quyết mâu thuẫn"),("Một cơ sở để hình thành lợi ích kinh tế","Quan hệ sản xuất và vị trí của chủ thể trong hệ thống sản xuất"),("Vai trò của Nhà nước trong quan hệ lợi ích","Điều hòa, bảo vệ lợi ích hợp pháp và xử lý mâu thuẫn"),("Tăng trưởng kinh tế cần gắn với","Tiến bộ, công bằng xã hội và phát triển bền vững"),("Kinh tế nhà nước có mối quan hệ với nền kinh tế","Gắn bó hữu cơ với toàn bộ nền kinh tế"),("Một hướng hoàn thiện thể chế được nêu","Hoàn thiện pháp luật về hợp đồng và giải quyết tranh chấp dân sự") ]},
{"title":"Công nghiệp hóa, hiện đại hóa và hội nhập kinh tế quốc tế","short":"CNH-HĐH & hội nhập","intro":"Tập trung khái niệm cách mạng công nghiệp, công nghiệp hóa, mô hình và hội nhập quốc tế.","sections":[
("Cách mạng công nghiệp","Là những bước phát triển nhảy vọt về chất trình độ của tư liệu lao động trên cơ sở phát minh đột phá về kỹ thuật và công nghệ, kéo theo thay đổi căn bản về phân công lao động xã hội và nâng cao năng suất lao động."),
("Công nghiệp hóa","Là quá trình chuyển đổi nền sản xuất xã hội từ dựa trên lao động thủ công là chính sang nền sản xuất xã hội dựa chủ yếu trên lao động bằng máy móc nhằm tạo ra năng suất lao động xã hội cao."),
("Hiện đại hóa","Là quá trình ứng dụng và trang bị những thành tựu khoa học - công nghệ tiên tiến, hiện đại vào các ngành, lĩnh vực kinh tế và đời sống xã hội."),
("Công nghiệp hóa, hiện đại hóa ở Việt Nam","Gắn với phát triển lực lượng sản xuất, ứng dụng khoa học - công nghệ, nâng cao năng suất, chất lượng, hiệu quả và sức cạnh tranh; đồng thời phát triển bền vững và gắn với hội nhập quốc tế."),
("Hội nhập kinh tế quốc tế","Là quá trình gắn kết nền kinh tế quốc gia với kinh tế khu vực và thế giới thông qua các hoạt động hợp tác, trao đổi, thực hiện cam kết và tham gia các thể chế kinh tế quốc tế.")],
"facts":[("Cách mạng công nghiệp","Bước phát triển nhảy vọt về chất của tư liệu lao động dựa trên đột phá kỹ thuật và công nghệ"),("Cách mạng công nghiệp kéo theo","Thay đổi phân công lao động xã hội và nâng cao năng suất lao động"),("Công nghiệp hóa","Chuyển từ sản xuất chủ yếu bằng lao động thủ công sang dựa chủ yếu trên máy móc"),("Mục tiêu trực tiếp của công nghiệp hóa","Tạo ra năng suất lao động xã hội cao"),("Hiện đại hóa","Ứng dụng thành tựu khoa học - công nghệ tiên tiến, hiện đại vào sản xuất và đời sống"),("Công nghiệp hóa, hiện đại hóa ở Việt Nam gắn với","Phát triển lực lượng sản xuất và ứng dụng khoa học - công nghệ"),("Một yêu cầu của CNH-HĐH","Nâng cao năng suất, chất lượng, hiệu quả và sức cạnh tranh"),("Hội nhập kinh tế quốc tế","Gắn kết nền kinh tế quốc gia với kinh tế khu vực và thế giới"),("Hội nhập kinh tế quốc tế diễn ra thông qua","Hợp tác, trao đổi, thực hiện cam kết và tham gia thể chế kinh tế quốc tế"),("Một tác động tích cực của hội nhập","Mở rộng thị trường và cơ hội hợp tác, tiếp cận nguồn lực"),("Một thách thức của hội nhập","Sức ép cạnh tranh và nguy cơ phụ thuộc nếu năng lực nội tại yếu"),("Công nghiệp hóa cổ điển","Mô hình công nghiệp hóa khởi đầu sớm, gắn với cách mạng công nghiệp ở một số nước tư bản"),("Động lực quan trọng của CNH-HĐH hiện nay","Khoa học - công nghệ và đổi mới sáng tạo"),("Nguồn lực cho CNH-HĐH","Nguồn lực trong nước kết hợp hiệu quả với nguồn lực quốc tế"),("Phân công lao động xã hội thay đổi do cách mạng công nghiệp","Chuyên môn hóa và tổ chức sản xuất biến đổi sâu sắc"),("Năng suất lao động xã hội","Hiệu quả tạo ra sản phẩm trong một đơn vị lao động xã hội"),("CNH-HĐH phải gắn với phát triển bền vững","Kết hợp mục tiêu kinh tế, xã hội và môi trường"),("Hội nhập không đồng nghĩa với","Từ bỏ độc lập, tự chủ của nền kinh tế"),("Năng lực cạnh tranh quốc gia phụ thuộc vào","Năng suất, chất lượng thể chế, nguồn nhân lực, công nghệ và hạ tầng"),("Vai trò của nguồn nhân lực trong CNH-HĐH","Tiếp thu, làm chủ và sáng tạo công nghệ"),("Chuyển đổi số hỗ trợ CNH-HĐH thông qua","Ứng dụng công nghệ số để đổi mới quản trị và quy trình sản xuất"),("Liên kết kinh tế quốc tế có thể giúp","Mở rộng chuỗi cung ứng và tiếp cận thị trường"),("Rủi ro khi hội nhập thiếu chuẩn bị","Doanh nghiệp trong nước suy giảm khả năng cạnh tranh"),("Một định hướng khi hội nhập","Chủ động, tích cực, đa phương hóa và đa dạng hóa quan hệ kinh tế"),("Mục tiêu tổng quát của CNH-HĐH","Xây dựng cơ sở vật chất - kỹ thuật và nâng cao trình độ phát triển của nền kinh tế") ]}
]

# Generate 25 distinct, chapter-specific recall questions from each chapter's verified concept list.
def build_questions(ch):
    facts=ch['facts']; qs=[]
    for i,(term,answer) in enumerate(facts):
        distractors=[]
        for step in (3,7,11):
            candidate=facts[(i+step)%len(facts)][1]
            if candidate!=answer and candidate not in distractors: distractors.append(candidate)
        while len(distractors)<3: distractors.append(facts[(i+len(distractors)+1)%len(facts)][1])
        opts=[answer]+distractors[:3]
        # Stable per-question shuffle seed so answer positions are consistent across reruns.
        random.Random(1000+i).shuffle(opts)
        qs.append({'q':f"Nội dung nào sau đây mô tả đúng: **{term}**?",'opts':opts,'answer':answer,'why':f"Đáp án đúng: {answer}. Hãy ghi nhớ cặp khái niệm - nội dung này và đối chiếu phần lý thuyết của chương."})
    return qs

for ch in CHAPTERS: ch['questions']=build_questions(ch)

if 'page' not in st.session_state: st.session_state.page='Tổng quan'
if 'done_chapters' not in st.session_state: st.session_state.done_chapters={}
if 'wrong' not in st.session_state: st.session_state.wrong=[]
if 'history' not in st.session_state: st.session_state.history=[]
if 'answers' not in st.session_state: st.session_state.answers={}
if 'exam' not in st.session_state: st.session_state.exam=None
if 'flash_index' not in st.session_state: st.session_state.flash_index=0

with st.sidebar:
    st.markdown("<div style='text-align:center;padding:8px 0 18px'><div style='font-size:38px'>🌸</div><div style='font-size:20px;font-weight:800;color:#995477'>PINK STUDY</div><div class='muted'>KINH TẾ CHÍNH TRỊ MÁC - LÊNIN</div></div>",unsafe_allow_html=True)
    pages=['Tổng quan','Lộ trình học','Học lý thuyết','Kiểm tra chương','Phòng thi thử 60 phút','Flashcard','Sổ tay câu sai','Tổng kết & mẹo thi']
    for p in pages:
        if st.button(('✦  ' if st.session_state.page==p else '　')+p,key='nav_'+p,use_container_width=True): st.session_state.page=p; st.rerun()
    st.markdown('---')
    st.caption('Tiến độ được lưu trong phiên trình duyệt Streamlit. Tải lại hoặc mở phiên mới có thể làm mất dữ liệu.')

page=st.session_state.page

if page=='Tổng quan':
    st.markdown("<div class='hero'><div class='kicker'>YOUR STUDY SPACE · 2026</div><h1 style='color:#70445f;margin:8px 0'>Học chắc từng chương. Tự tin vào phòng thi. 🌷</h1><p style='color:#795a70;max-width:680px'>Một lộ trình từ mất gốc đến hiểu bản chất, ghi nhớ có hệ thống và luyện đề 60 phút.</p><span class='pill'>6 chương</span><span class='pill'>150 câu ôn chương</span><span class='pill'>50 câu thi thử</span><span class='pill'>Flashcard</span></div>",unsafe_allow_html=True)
    st.write('')
    completed=len(st.session_state.done_chapters)
    c1,c2,c3,c4=st.columns(4)
    c1.markdown(f"<div class='card'><div class='kicker'>CHƯƠNG ĐÃ ÔN</div><div class='big'>{completed}/6</div><div class='muted'>Hoàn thành bài kiểm tra chương</div></div>",unsafe_allow_html=True)
    c2.markdown(f"<div class='card'><div class='kicker'>CÂU SAI ĐÃ LƯU</div><div class='big'>{len(st.session_state.wrong)}</div><div class='muted'>Cần luyện tập thêm</div></div>",unsafe_allow_html=True)
    c3.markdown(f"<div class='card'><div class='kicker'>LẦN THI THỬ</div><div class='big'>{len(st.session_state.history)}</div><div class='muted'>Kết quả trong phiên</div></div>",unsafe_allow_html=True)
    c4.markdown(f"<div class='card'><div class='kicker'>NGÂN HÀNG CÂU HỎI</div><div class='big'>150</div><div class='muted'>25 câu mỗi chương</div></div>",unsafe_allow_html=True)
    st.subheader('Bản đồ 6 chương')
    for i,ch in enumerate(CHAPTERS):
        done=st.session_state.done_chapters.get(str(i))
        a,b=st.columns([5,1]); a.markdown(f"**Chương {i+1}. {ch['title']}**  <span class='muted'> · {ch['intro']}</span>",unsafe_allow_html=True); b.markdown(f"<span class='pill'>{'Đã kiểm tra' if done else 'Chưa hoàn thành'}</span>",unsafe_allow_html=True)
        st.progress(1.0 if done else 0.0)
    st.info('Gợi ý bắt đầu: học Chương 1 trước để nắm cách tư duy, sau đó học Chương 2 và 3 thật chắc. Chương 3 thường có nhiều khái niệm và công thức cần phân biệt.')

elif page=='Lộ trình học':
    st.title('🗺️ Lộ trình học từ mất gốc')
    st.markdown("<div class='card'><b>Vòng học 4 bước cho mỗi chương</b><ol><li><b>Hiểu:</b> đọc phần giải thích đơn giản, tự diễn đạt lại bằng lời của mình.</li><li><b>Ghi nhớ:</b> chốt định nghĩa, từ khóa, cặp khái niệm dễ nhầm.</li><li><b>Kiểm tra:</b> làm 25 câu không nhìn tài liệu.</li><li><b>Sửa lỗi:</b> đọc giải thích, ghi câu sai vào sổ tay và làm lại.</li></ol></div>",unsafe_allow_html=True)
    for i,ch in enumerate(CHAPTERS):
        with st.expander(f"Tuần tự học · Chương {i+1}: {ch['title']}",expanded=(i==0)):
            st.write(ch['intro']); st.write('**Việc cần làm:**')
            st.checkbox('Đọc toàn bộ phần lý thuyết',key=f'plan_{i}_1'); st.checkbox('Tự nói lại 5 ý quan trọng không nhìn tài liệu',key=f'plan_{i}_2'); st.checkbox('Làm bài kiểm tra 25 câu',key=f'plan_{i}_3'); st.checkbox('Ôn lại các câu sai',key=f'plan_{i}_4')
    st.warning('Đừng chỉ đọc đi đọc lại. Hãy đóng tài liệu và thử tự nhớ lại. Khả năng gọi kiến thức ra khỏi trí nhớ mới là thứ cần cho bài thi.')

elif page=='Học lý thuyết':
    st.title('📚 Học lý thuyết')
    idx=st.selectbox('Chọn chương',range(6),format_func=lambda x:f"Chương {x+1} · {CHAPTERS[x]['title']}")
    ch=CHAPTERS[idx]
    st.markdown(f"<div class='hero'><div class='kicker'>CHƯƠNG {idx+1}</div><h2 style='color:#70445f'>{ch['title']}</h2><p style='color:#795a70'>{ch['intro']}</p></div>",unsafe_allow_html=True)
    for heading,body in ch['sections']:
        with st.expander(heading,expanded=True): st.write(body)
    st.subheader('🎯 Tự kiểm tra nhanh')
    st.caption('Hãy thử trả lời bằng lời của bạn trước khi mở đáp án.')
    for term,answer in ch['facts'][:8]:
        with st.expander(term): st.success(answer)
    if st.button('Đi đến bài kiểm tra chương này',type='primary'): st.session_state.quiz_chapter=idx; st.session_state.page='Kiểm tra chương'; st.rerun()

elif page=='Kiểm tra chương':
    st.title('✍️ Kiểm tra cuối chương')
    idx=st.selectbox('Chọn chương muốn kiểm tra',range(6),format_func=lambda x:f"Chương {x+1} · {CHAPTERS[x]['title']}",key='quiz_select')
    ch=CHAPTERS[idx]
    if st.button('Bắt đầu / làm lại bài kiểm tra 25 câu',type='primary'):
        st.session_state.active_quiz={'chapter':idx,'order':random.sample(range(25),25),'submitted':False,'responses':{}}; st.rerun()
    quiz=st.session_state.get('active_quiz')
    if quiz and quiz['chapter']==idx:
        st.progress(len(quiz['responses'])/25); st.caption(f"Đã trả lời {len(quiz['responses'])}/25 câu")
        with st.form('chapter_quiz_form'):
            for n,qid in enumerate(quiz['order']):
                q=ch['questions'][qid]; st.markdown(f"**Câu {n+1}.** {q['q']}")
                choice=st.radio('Chọn một đáp án',q['opts'],key=f"cq_{idx}_{qid}",index=None,label_visibility='collapsed')
                if choice: quiz['responses'][str(qid)]=choice
                st.markdown('---')
            submitted=st.form_submit_button('Nộp bài và xem kết quả',type='primary')
        if submitted:
            score=0; wrong=[]
            for qid in quiz['order']:
                q=ch['questions'][qid]; picked=quiz['responses'].get(str(qid))
                if picked==q['answer']: score+=1
                else: wrong.append({'chapter':idx,'question':q['q'],'picked':picked or 'Chưa trả lời','answer':q['answer'],'why':q['why']})
            st.session_state.wrong.extend(wrong); st.session_state.done_chapters[str(idx)]={'score':score,'total':25,'date':time.strftime('%d/%m/%Y %H:%M')}; quiz['submitted']=True; quiz['score']=score; quiz['wrong']=wrong
        if quiz.get('submitted'):
            score=quiz['score']; st.markdown(f"<div class='card'><div class='kicker'>KẾT QUẢ CHƯƠNG {idx+1}</div><div class='big'>{score}/25 · {score*4}%</div><div class='muted'>{'Rất tốt! Tiếp tục duy trì.' if score>=22 else 'Khá ổn, hãy tập trung sửa câu sai.' if score>=18 else 'Cần học lại phần lý thuyết trước khi chuyển chương.'}</div></div>",unsafe_allow_html=True)
            st.progress(score/25)
            for item in quiz['wrong']:
                st.error(f"{item['question']}\n\nBạn chọn: {item['picked']}\n\nĐáp án: {item['answer']}\n\nGiải thích: {item['why']}")
            if not quiz['wrong']: st.success('Bạn đã trả lời đúng toàn bộ 25 câu!')

elif page=='Phòng thi thử 60 phút':
    st.title('⏱️ Phòng thi thử · 60 phút · 50 câu')
    st.markdown("<div class='card'><b>Quy chế mô phỏng</b><ul><li>50 câu trắc nghiệm, mỗi câu 1 lựa chọn.</li><li>Thời gian làm bài: 60 phút.</li><li>Có thể đánh dấu câu cần xem lại.</li><li>Hết giờ hệ thống tự động nộp bài.</li><li>Chỉ hiện đáp án và giải thích sau khi nộp.</li></ul></div>",unsafe_allow_html=True)
    if st.session_state.exam is None:
        st.warning('Khi bắt đầu, đồng hồ sẽ chạy. Hãy chuẩn bị và chỉ nhấn bắt đầu khi sẵn sàng.')
        if st.button('🚀 BẮT ĐẦU THI THỬ',type='primary'):
            pool=[]
            for ci,ch in enumerate(CHAPTERS):
                for q in ch['questions']: pool.append((ci,q))
            selected=random.sample(pool,50)
            st.session_state.exam={'start':time.time(),'end':time.time()+3600,'items':selected,'responses':{},'flags':[],'submitted':False,'results_saved':False}
            st.rerun()
    else:
        ex=st.session_state.exam
        if not ex['submitted']:
            remaining=max(0,int(ex['end']-time.time()))
            if remaining>0: st_autorefresh(interval=1000,key='exam_clock')
            mins,secs=divmod(remaining,60)
            st.markdown(f"<div class='hero'><div class='kicker'>THỜI GIAN CÒN LẠI</div><div style='font-size:42px;font-weight:800;color:#7b4267;font-variant-numeric:tabular-nums'>{mins:02d}:{secs:02d}</div><div style='color:#795a70'>Đã trả lời {len(ex['responses'])}/50 câu</div></div>",unsafe_allow_html=True)
            if remaining==0: ex['submitted']=True; ex['auto']=True; st.rerun()
            st.progress(len(ex['responses'])/50)
            with st.form('full_exam'):
                for i,(ci,q) in enumerate(ex['items']):
                    st.markdown(f"**Câu {i+1}.** <span class='pill'>Chương {ci+1}</span> {q['q']}",unsafe_allow_html=True)
                    picked=st.radio('Chọn đáp án',q['opts'],key=f"exam_{i}",index=None,label_visibility='collapsed')
                    if picked: ex['responses'][str(i)]=picked
                    flag=st.checkbox('Đánh dấu xem lại',key=f'flag_{i}')
                    if flag and i not in ex['flags']: ex['flags'].append(i)
                    if not flag and i in ex['flags']: ex['flags'].remove(i)
                    st.markdown('---')
                submit=st.form_submit_button('NỘP BÀI THI',type='primary')
            if submit: ex['submitted']=True; ex['auto']=False; st.rerun()
        if ex['submitted']:
            correct=0; details=[]; by_ch={i:[0,0] for i in range(6)}
            for i,(ci,q) in enumerate(ex['items']):
                picked=ex['responses'].get(str(i)); ok=picked==q['answer']; correct+=int(ok); by_ch[ci][0]+=int(ok); by_ch[ci][1]+=1
                if not ok: details.append((i+1,ci,q,picked))
            st.markdown(f"<div class='card'><div class='kicker'>KẾT QUẢ BÀI THI</div><div class='big'>{correct}/50 · {correct*0.2:.1f}/10 điểm</div><div class='muted'>{'Bài thi tự động nộp khi hết giờ.' if ex.get('auto') else 'Bài thi đã được nộp.'}</div></div>",unsafe_allow_html=True)
            st.progress(correct/50)
            if not ex.get('results_saved'):
                st.session_state.history.append({'score':correct,'date':time.strftime('%d/%m/%Y %H:%M')})
                for no,ci,q,picked in details:
                    st.session_state.wrong.append({'chapter':ci,'question':q['q'],'picked':picked or 'Chưa trả lời','answer':q['answer'],'why':q['why']})
                ex['results_saved']=True
            st.subheader('Kết quả theo chương')
            for ci,(got,total) in by_ch.items(): st.write(f"Chương {ci+1}: **{got}/{total}**"); st.progress(got/total if total else 0)
            st.subheader(f'Câu cần xem lại ({len(details)})')
            for no,ci,q,picked in details:
                with st.expander(f"Câu {no} · Chương {ci+1}"):
                    st.write(q['q']); st.write('Bạn chọn:',picked or 'Chưa trả lời'); st.success('Đáp án: '+q['answer']); st.caption(q['why'])
            if st.button('Tạo đề thi thử mới'): st.session_state.exam=None; st.rerun()

elif page=='Flashcard':
    st.title('🃏 Flashcard ghi nhớ nhanh')
    allcards=[]
    for ci,ch in enumerate(CHAPTERS):
        for term,answer in ch['facts']: allcards.append((ci,term,answer))
    ci,term,answer=allcards[st.session_state.flash_index%len(allcards)]
    st.caption(f"Thẻ {st.session_state.flash_index%len(allcards)+1}/{len(allcards)} · Chương {ci+1}")
    st.markdown(f"<div class='hero' style='text-align:center;min-height:230px;display:flex;flex-direction:column;justify-content:center'><div class='kicker'>GỢI NHỚ KHÁI NIỆM</div><h2 style='color:#70445f'>{term}</h2><p style='color:#795a70'>Hãy tự trả lời trước khi lật thẻ</p></div>",unsafe_allow_html=True)
    if st.button('👀 Lật thẻ xem đáp án',use_container_width=True): st.session_state.show_flash=True
    if st.session_state.get('show_flash'): st.success(answer)
    a,b=st.columns(2)
    if a.button('← Thẻ trước'): st.session_state.flash_index=max(0,st.session_state.flash_index-1); st.session_state.show_flash=False; st.rerun()
    if b.button('Thẻ tiếp theo →'): st.session_state.flash_index+=1; st.session_state.show_flash=False; st.rerun()
    st.info('Mẹo: trả lời thành tiếng hoặc viết ra giấy trước khi lật thẻ. Nếu không nhớ, đánh dấu để quay lại sau.')

elif page=='Sổ tay câu sai':
    st.title('🧩 Sổ tay câu sai')
    if not st.session_state.wrong: st.success('Chưa có câu sai nào được lưu. Hãy làm bài kiểm tra để xây dựng sổ tay cá nhân. 🌸')
    else:
        st.caption(f"Tổng cộng {len(st.session_state.wrong)} lượt câu sai/chưa trả lời trong phiên này.")
        for i,item in enumerate(reversed(st.session_state.wrong)):
            with st.expander(f"Chương {item['chapter']+1} · {item['question']}"):
                st.write('Bạn chọn:',item['picked']); st.success('Đáp án đúng: '+item['answer']); st.caption(item['why'])
        if st.button('Xóa sổ tay câu sai'): st.session_state.wrong=[]; st.rerun()

else:
    st.title('🎀 Tổng kết & mẹo làm bài')
    st.subheader('Các cặp khái niệm cần phân biệt')
    pairs=[('Giá trị sử dụng','Công dụng, khả năng thỏa mãn nhu cầu của hàng hóa.'),('Giá trị','Lao động xã hội kết tinh trong hàng hóa.'),('Lao động cụ thể','Tạo ra giá trị sử dụng.'),('Lao động trừu tượng','Tạo ra giá trị hàng hóa.'),('Tư bản bất biến (c)','Giá trị tư liệu sản xuất được bảo toàn và chuyển vào sản phẩm.'),('Tư bản khả biến (v)','Đầu tư mua sức lao động, tạo ra giá trị mới và giá trị thặng dư.'),('Giá trị thặng dư tuyệt đối','Tăng bằng cách kéo dài ngày lao động.'),('Giá trị thặng dư tương đối','Tăng bằng cách rút ngắn thời gian lao động tất yếu.'),('Tích tụ tư bản','Tăng quy mô tư bản cá biệt bằng tích lũy.'),('Tập trung tư bản','Hợp nhất các tư bản đã có.')]
    for a,b in pairs:
        with st.expander(a): st.write(b)
    st.subheader('Công thức cần thuộc')
    st.markdown("<div class='card'><h3 style='color:#995477'>m’ = (m / v) × 100%</h3><p>Tỷ suất giá trị thặng dư = giá trị thặng dư / tư bản khả biến × 100%.</p><hr><h3 style='color:#995477'>T’ = T + ΔT</h3><p>Giá trị tiền thu về lớn hơn số tiền ứng trước; phần tăng thêm là giá trị thặng dư.</p></div>",unsafe_allow_html=True)
    st.subheader('Chiến thuật 60 phút')
    st.markdown("1. Lướt nhanh toàn đề, nhận diện câu dễ.\n2. Làm câu chắc chắn trước, không mắc kẹt quá lâu ở một câu.\n3. Đánh dấu câu phân vân để quay lại.\n4. Dành 5-8 phút cuối rà soát câu bỏ trống và câu đánh dấu.\n5. Đọc kỹ từ khóa phủ định như *không*, *chỉ*, *luôn luôn*, *chủ yếu*.\n\n**Lưu ý:** đây là chiến thuật quản lý thời gian gợi ý, không phải quy định chính thức của kỳ thi.")
    st.subheader('Kết quả luyện tập trong phiên')
    if st.session_state.history:
        for h in st.session_state.history: st.write(f"{h['date']} · {h['score']}/50 ({h['score']*0.2:.1f}/10)")
    else: st.caption('Bạn chưa hoàn thành bài thi thử nào.')

st.markdown("<div style='text-align:center;color:#b28ba3;font-size:11px;padding:30px 0 10px'>PINK STUDY · HỌC HIỂU, NHỚ LÂU, THI TỰ TIN ✿</div>",unsafe_allow_html=True)
