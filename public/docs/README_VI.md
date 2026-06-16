<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">Bắt đầu / Giữa / Kết thúc</h1>

<p align="center">
  <a href="https://github.com/bastndev/skills/blob/main/README.md">English 🇺🇸</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ES.md">Español 🇪🇸</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ZH.md">中文 🇨🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_DE.md">Deutsch 🇩🇪</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_FR.md">Français 🇫🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_JA.md">日本語 🇯🇵</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_KO.md">한국어 🇰🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_PT.md">Português 🇧🇷</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_RU.md">Русский 🇷🇺</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_HI.md">हिन्दी 🇮🇳</a> | 
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_AR.md">العربية 🇸🇦</a>
</p>

<br>

<p align="center">
  Tự tin khởi tạo các dự án mới. Tinh chỉnh và củng cố chúng một cách lặp đi lặp lại khi chúng phát triển. Thực hiện tái cấu trúc sâu, an toàn khi kiến trúc cần tiến hóa.
</p>

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

## Ba Giai Đoạn

| Giai đoạn | Mục đích | Khả năng chính | Ví dụ | Trạng thái |
| --- | --- | --- | --- | --- |
| **Start** | Khởi tạo dự án | Tạo cấu trúc thư mục sẵn sàng cho sản xuất, khởi tạo framework, áp dụng thực tiễn tốt nhất ngay từ commit đầu tiên. | `start-nextjs`... | Dự kiến |
| **Middle** | Cải tiến liên tục | Nâng cao UI/UX, củng cố bảo mật, tăng hiệu suất, dọn dẹp logic, loại bỏ code chết. | TBD | Dự kiến |
| **End** | Kiểm toán & Tái cấu trúc | Phân tích kiến trúc và chất lượng đầy đủ. Kế hoạch từng giai đoạn được thực thi **chỉ khi có sự chấp thuận rõ ràng**. | `refactor-project` | ✅ Có sẵn |

## Các Kỹ Năng (Skills) Hiện Có

| Skill | Mô tả |
| --- | --- |
| **[end](../../skills/end/README.md)** | **`refactor-project`** — Hiểu dự án của bạn từ đầu đến cuối. Cung cấp chẩn đoán rõ ràng với các tài liệu tham khảo cụ thể. Khuyến nghị hướng kiến trúc phù hợp và xây dựng kế hoạch thực thi có trật tự. Bạn luôn giữ quyền kiểm soát hoàn toàn.<br><br>→ [Tài liệu đầy đủ & ví dụ](../../skills/end/README.md) |

> **Lưu ý:** Mỗi skill đều có README chi tiết riêng. Trang gốc cung cấp tổng quan cấp cao; hãy xem `../../skills/<skill>/README.md` để biết cách sử dụng sâu, các ví dụ về báo cáo và đảm bảo.

## Cài đặt

```bash
# Thêm skill hiện tại (End / refactor-project)
npx skills add bastndev/skills --skill end
```

Các skill trong tương lai sẽ được cài đặt theo cách tương tự:

```bash
npx skills add bastndev/skills --skill start-nextjs
```

## Cách Skill End Hoạt Động

1. **Phân tích trước** — Lập bản đồ các điểm vào và hiểu dự án. **Không có tệp nào bị sửa đổi.**
2. **Báo cáo có cấu trúc** — Các phát hiện rõ ràng trong bốn danh mục (Lỗi đã xác nhận kèm mức độ nghiêm trọng, Rủi ro, Cơ hội tái cấu trúc, Nợ kỹ thuật) + khuyến nghị kiến trúc và kế hoạch có thứ tự. Tất cả các mục đều bao gồm các tham chiếu tệp và dòng cụ thể.
3. **Bạn cho phép từng giai đoạn** — Nó thực hiện **chính xác một giai đoạn** tại một thời điểm. Sau mỗi giai đoạn, bạn nhận được một bản tóm tắt chính xác về các thay đổi, xác thực được thực hiện và danh sách các giai đoạn còn lại.
4. **Kiểm soát và an toàn tuyệt đối** — Không bao giờ tạo thử nghiệm nếu dự án không có. Không bao giờ thêm phần phụ thuộc hoặc thay đổi trình quản lý gói mà không có sự cho phép. Tôn trọng công việc chưa được cam kết của bạn và luôn duy trì hành vi hiện tại trừ khi sửa một lỗi chính đáng.

Để biết quy trình làm việc đầy đủ, định dạng báo cáo chính xác, các quy tắc quyết định kiến trúc và tất cả các đảm bảo an toàn, hãy đọc tài liệu skill chuyên dụng:

→ **[End – Refactor Project](../../skills/end/README.md)**

Đặc tả nội bộ đầy đủ nằm trong [skills/end/SKILL.md](../../skills/end/SKILL.md).

## Lộ trình

- **Các Skill Start** — Dàn giáo dự án bằng một lệnh cho các ngăn xếp phổ biến (Next.js, Vite, FastAPI, v.v.)
- **Các Skill Middle** — Các bộ cải tiến tập trung theo yêu cầu (hiệu suất, bảo mật, UX, loại bỏ mã chết, v.v.)
- **Mở rộng End** — Nhiều thời gian chạy hơn, các chế độ tái cấu trúc chuyên dụng bổ sung và các tiện ích.

Mỗi skill sẽ có tài liệu chuyên dụng riêng (giống như [End – Refactor Project](../../skills/end/README.md) hiện tại).

---

<br>

<div align="center">
  <p align="center">
  <sub>Được xây dựng cho các nhà phát triển muốn tác nhân AI của họ hành động với kỷ luật của một kỹ sư cấp cao.</sub>
</p>

_If you find any bugs or have feedback, feel free to [open an issue](https://github.com/bastndev/skills/issues/new)._

<sub>Made in 🇵🇪 by <a href="https://gohit.xyz">Gohit X</a> · Licensed under <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
