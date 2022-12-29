# Data Augmentation for Span Detection for Aspect-Based Sentiment Analysis in Vietnamese

Tiến hành tăng cường dữ liệu dữ liệu nhằm cải thiện hiệu suất cho Task Span Detection trên bộ dữ liệu tiếng Việt.

## Mục đích
Nhằm cải thiện hiệu suất mô hình so với trước và giải quyết vấn đề mất cân bằng trong bộ dữ liệu UIT-ViSD4SA.

## Data
Dựa trên bộ dữ liệu có sẵn đã công bố được lưu trữ trên Github [UIT-ViSD4SA](https://github.com/kimkim00/UIT-ViSD4SA).

Quá trình phát triển bộ dữ liệu tham khảo tại paper [Span Detection for Aspect-Based Sentiment Analysis in Vietnamese](https://aclanthology.org/2021.paclic-1.34.pdf).

## Tăng cường dữ liệu
Bằng 2 cách sau:
  1. Tiến hành thu thập dữ liệu tại các website thương mại điện tử về điện thoại thông minh và gán nhãn theo guideline có sẵn trong paper trên.
  2. Kỹ thuật Easy Data Augmentation (EDA) bao gồm các thao tác sau: 
  * Chèn ngẫu nhiên (Random Insertion)
  * Hoán đổi ngẫu nhiên (Random Swap)
  * Xóa ngẫu nhiên (Random Deletion)
  * Thay từ đồng nghĩa (Synonym replacement)
  
  Tham khảo tại paper [EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks](https://arxiv.org/abs/1901.11196) trên bộ dữ liệu tiếng Anh và paper [Empirical Study of Text Augmentation on Social Media Text in Vietnamese](https://aclanthology.org/2020.paclic-1.53/) trên bộ dữu liệu tiếng Việt.
  
## Mô hình
Sử dụng transformer với mô hình đã được đạo tạo trước [phoBERT](https://aclanthology.org/2020.findings-emnlp.92/) trên bộ dữ liệu tiếng Việt.
Code sử dụng tham khảo tại [repo](https://github.com/datnnt1997/ViSA).

## Kết quả
Mô hình phoBERT có cải thiện hiệu suất đôi chút so với bài báo gốc trên tập dữu liệu gốc và hiệu suất tăng 3.1% (f1-score macro) trên tập dữ liệu tăng cường cùng mô hình phoBERT.

## Lưu ý
* Đây chỉ là phương pháp tăng cường dữ liệu đơn giản, hiện tại có nhiều mô hình tăng cường dữ liệu với hiệu suất cao hơn.
* Phương pháp này làm tăng hiệu suất 1 số nhãn nhưng cũng là giảm hiệu suất 1 số nhãn còn lại.
* Đây là đồ án môn học NLP - Là kết quả làm việc của các thành viên trong nhóm.
