# Review: Vietnamese (vi)

Method: blind back-translation (`review/vi.back.json`), comparison with source.json, full native read. Build: 0 hard errors.


## Meaning (10)

- **26**: Vậy làm sao trộm 388 triệu đô la mà không cần khóa? → Vậy làm sao trộm 388 triệu đô la mà không có khóa? — 'without the keys', not 'without needing'
- **53**: Một lưu ý. Mandiant chỉ xác định quyền truy cập đặc quyền của kẻ tấn công từ ngày 24 tháng Chín. → Một lưu ý. Mandiant chỉ xác định quyền truy cập đặc quyền của kẻ tấn công từ ngày 24 tháng 9 trở đi. — no earlier than 24 Sept (producer note); natural month form
- **63**: Đoạn mã đó đã lan ra. → Chính đoạn mã đó đã lan ra. — 'The same script'
- **70**: và rằng, tạm thời, họ đã loại trừ khả năng có người bên trong. → và rằng, tạm thời, họ đã loại trừ khả năng có người trong nội bộ tiếp tay. — 'người bên trong' ambiguous with the intruder ('someone inside' in cue 52); here it means insiders
- **80**: Nó làm giả các câu trả lời. → Nó giả mạo các câu trả lời. — 'forged' (giả mạo), not just 'faked'
- **92**: Một điều có thể làm lộ họ. Hãy nhớ lấy nó. → Một điều lẽ ra có thể làm lộ họ. Hãy ghi nhớ điều này. — 'could have given them away' (counterfactual)
- **138**: Mỗi lệnh chuyển bị trộm gom lại khoảng 1.000 mảnh coin. → Mỗi lệnh chuyển tiền bị trộm gom khoảng 1.000 mảnh coin nhỏ. — producer note: about 1,000 small pieces
- **142**: Không ai canh chừng chúng. → Không ai dò tìm chúng. — 'watching for them' = looking out for the fingerprints, not guarding
- **145**: Stablecoin được xử lý trước, vì stablecoin có thể bị đóng băng. → Stablecoin được chuyển đi trước tiên, vì stablecoin có thể bị đóng băng. — 'went first' = were moved first, not 'handled'
- **179**: Mười chín tháng sau, tiền lại chảy ra khỏi Bitget. → Mười chín tháng sau, tiền đang chảy ra khỏi Bitget. — 'lại' could read as 'again' (Bitget's money had never left before)

## Grammar (8)

- **10**: Nó nằm trong log. Từ 24 ngày trước đó. → Nó nằm trong log. Có từ 24 ngày trước đó. — fragment needed a verb ('dated')
- **21**: Vào thời điểm đó, là vụ trộm crypto lớn nhất trong năm. → Vào thời điểm đó, đây là vụ trộm crypto lớn nhất trong năm. — sentence lacked a subject
- **34**: Kiểm tra rủi ro xem xét nó. → Khâu kiểm tra rủi ro duyệt nó. — bare noun phrase as subject unnatural; kept short for 1.2 s
- **86**: Chỉ có một cách để biết nó có hiệu quả trên thực tế không. → Chỉ có một cách để biết cách này có hiệu quả trên thực tế hay không. — question frame incomplete
- **148**: Một phần Zcash biến vào một pool riêng tư, nơi không thể truy dấu. → Một phần Zcash biến mất vào một pool riêng tư, nơi không thể truy dấu. — 'biến vào' incomplete verb
- **156**: ZachXBT nói những kẻ rửa tiền đã nhờ hỗ trợ khách hàng → ZachXBT nói những kẻ rửa tiền đã nhờ bộ phận hỗ trợ khách hàng — 'nhờ hỗ trợ khách hàng' unclear
- **173**: Với Bitget, chưa chính phủ nào lên tiếng một lời. → Với Bitget, chưa chính phủ nào nói một lời. — 'lên tiếng một lời' redundant
- **182**: Nếu bạn có tiền trên Bitget, bạn không mất số tiền đó. → Nếu bạn có tiền trên Bitget, bạn đã không mất nó. — past: you didn't lose it

## Style (18)

- **11**: Để hiểu vì sao vụ này đau, hãy lùi lại 19 tháng. Tháng Hai năm 2025. → Để hiểu vì sao vụ này lại đau, hãy lùi lại 19 tháng. Tháng 2/2025. — natural month form (producer note); 'lại đau' reads naturally
- **19**: Nó sẽ quay lại ở phần cuối. → Ở cuối tập, nó sẽ quay trở lại. — 'phần cuối' vague; natural word order
- **20**: Ngày 24 tháng Chín năm 2026, sàn từng ra tay giúp đỡ lại trở thành sàn bị cướp. → Ngày 24/9/2026, sàn từng ra tay giúp đỡ lại trở thành sàn bị cướp. — natural date form instead of 'tháng Chín'
- **28**: Một sàn giữ phần lớn tiền trong ví lạnh. → Một sàn giao dịch giữ phần lớn tiền của mình trong ví lạnh. — 'Một sàn giữ phần lớn tiền' clipped
- **41**: Ngày 31 tháng Tám. Đó là hoạt động độc hại sớm nhất mà điều tra viên tìm thấy trong log. → Ngày 31 tháng 8. Đó là hoạt động độc hại sớm nhất mà điều tra viên tìm thấy trong log. — natural month form
- **44**: Một trong hai công cụ bên thứ ba mà Bitget dùng để bảo vệ hệ thống. → Một trong hai công cụ bên thứ ba mà Bitget dùng để bảo vệ hệ thống của mình. — 'its systems'
- **64**: Một máy thứ hai vào ngày 23 tháng Chín. → Máy thứ hai vào ngày 23 tháng 9. — natural month form; 'Một máy thứ hai' unnatural
- **75**: Giờ họ đã đứng ngay cạnh tiền. → Giờ họ đã đứng ngay cạnh số tiền. — 'cạnh tiền' clipped
- **93**: Rồi, không có gì. Gần nửa tiếng. → Rồi, không có gì cả. Suốt gần nửa tiếng. — 'For almost half an hour'
- **102**: Kiểm soát rủi ro đã chặn rút tiền với mọi khách hàng trên nền tảng. → Kiểm soát rủi ro đã chặn lệnh rút của mọi khách hàng trên nền tảng. — 'chặn rút tiền với' unnatural
- **131**: chi tiết kỳ lạ nằm ngay ở đó. → chi tiết kỳ lạ ấy nằm ngay ở đó. — 'the odd detail' already introduced
- **152**: Vào tháng Mười Một, số Bitcoin bắt đầu di chuyển trở lại. → Vào tháng 11, số Bitcoin đó bắt đầu di chuyển trở lại. — natural month form; 'the Bitcoin' = that Bitcoin
- **160**: Từ vụ khai thác Kelp DAO hồi tháng Tư. → Từ vụ khai thác Kelp DAO hồi tháng 4. — natural month form
- **175**: Điều đó đưa chúng ta trở lại khoản vay. → Điều đó đưa chúng ta trở lại khoản vay ấy. — 'that loan'
- **176**: Tháng Hai năm 2025, khi Bybit bị cướp, Bitget gửi 40.000 ether ngay trong ngày. → Tháng 2/2025, khi Bybit bị cướp, Bitget gửi 40.000 ether ngay trong ngày. — natural month form
- **184**: Đến ngày 2 tháng Mười, mọi lệnh rút đã hoạt động lại. → Đến ngày 2/10, mọi lệnh rút đã hoạt động lại. — natural date form
- **195**: Và khi báo động cuối cùng vang lên, sàn đã khóa khách hàng của mình, → Và khi báo động cuối cùng vang lên, sàn đã chặn khách hàng của mình, — 'khóa khách hàng' (lock the customers) odd
- **197**: Tôi là Thomas Archer. Đây là Siphon Files. → Tôi là Thomas Archer. Bạn vừa xem Siphon Files. — conventional sign-off for 'This was Siphon Files'

## Terminology (2)

- **49**: Đoạn mã tìm thấy mật khẩu cơ sở dữ liệu, để dưới dạng văn bản thô. → Đoạn mã tìm thấy mật khẩu cơ sở dữ liệu, lưu dưới dạng văn bản thuần. — 'văn bản thuần' is the usual term for plain text
- **72**: Từ đó, họ di chuyển ngang, sang máy chủ tác vụ ví chính thức. → Từ đó, họ di chuyển ngang, sang máy chủ tác vụ ví đang vận hành. — 'production' = live system, 'chính thức' read as 'official'

## Uncertain / notes
- All month names now in the normal numeric form (tháng 2/2025, 24/9/2026, tháng 8, tháng 9, tháng 4, tháng 11, 2/10); values unchanged.
- 72 'máy chủ tác vụ ví đang vận hành' for 'production wallet job server'; some devs would write 'production' in English.
- 113/114 fragments kept clipped ('Không người thứ hai.') because cue 113 is 0.9 s.
- 116 '2 giờ 39 phút' vs 'tiếng' elsewhere: both natural, kept.
