<p align="center">
  <img src="https://raw.githubusercontent.com/bastndev/skills/main/public/logo.webp" width="180" />
</p>

<h1 align="center">[Bắt đầu] / Giữa / [Kết thúc]</h1>

<p align="center">
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ES.md">Español 🇪🇸</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_ZH.md">中文 🇨🇳</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_DE.md">Deutsch 🇩🇪</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_FR.md">Français 🇫🇷</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_JA.md">日本語 🇯🇵</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_KO.md">한국어 🇰🇷</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_PT.md">Português 🇧🇷</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_RU.md">Русский 🇷🇺</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_VI.md">Tiếng Việt 🇻🇳</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_HI.md">हिन्दी 🇮🇳</a> |
  <a href="https://github.com/bastndev/skills/blob/main/public/docs/README_AR.md">العربية 🇸🇦</a>
</p>

<br>

<p align="center">
  Tự tin khởi động các dự án mới. Lặp đi lặp lại việc tinh chỉnh và củng cố chúng khi chúng phát triển. Thực hiện tái cấu trúc (refactoring) sâu và an toàn khi kiến trúc cần phải tiến hóa.
</p>

<p align="center">
  <a href="https://skills.sh/bastndev/skills">
    <img src="https://skills.sh/b/bastndev/skills" alt="skills.sh">
  </a>
</p>

```
npx skills add bastndev/skills
```

<br>

## Ba Giai Đoạn

| Giai đoạn | Mục đích | Các Khả Năng Chính | Các Skill Ví dụ | Trạng thái |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------ |
| **Start** (Bắt đầu) | Bắt đầu một dự án — tạo cấu trúc mới, hoặc học hỏi từ một dự án hiện có | Tạo cấu trúc và cấu hình sẵn sàng cho sản xuất (production) từ commit số 1. Hoặc phân tích kiến trúc & các gói thư viện của một codebase hiện có và ghi tài liệu, để bạn có thể tái sử dụng những pattern hiệu quả vào dự án của riêng mình. | `start-package`, `skrapi`       | ㅤㅤ✅ |
| **Middle** (Giữa) | Cải tiến liên tục & trau chuốt | Nâng cao UI/UX, củng cố bảo mật, tăng cường hiệu suất, dọn dẹp logic và loại bỏ mã chết (dead code) trong suốt quá trình phát triển tích cực. | Công cụ cải tiến mục tiêu (Đang cập nhật) | Đã lên kế hoạch |
| **End** (Kết thúc) | Kiểm toán, chẩn đoán & tái cấu trúc an toàn | Phân tích toàn bộ kiến trúc & chất lượng. Các phát hiện được phân loại kèm theo bằng chứng ở mức độ file. Kế hoạch theo từng giai đoạn ưu tiên được thực thi **chỉ khi có sự chấp thuận rõ ràng**. Giữ nguyên hành vi. Hỗ trợ đa môi trường runtime. | `end` | ㅤㅤ✅ |

## Các Skill Hiện Có

Được liệt kê theo thứ tự tự nhiên mà bạn sẽ tiếp cận — **Start** (Bắt đầu) một thứ gì đó mới (hoặc nghiên cứu một codebase hiện có để lấy cảm hứng), tinh chỉnh nó ở **Middle** (Giữa), và củng cố nó vào **End** (Kết thúc).

| Skill | Mô tả |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[start-package](../../skills/start-package/README.md)** | _Start_ (Bắt đầu) — Tạo cấu trúc một gói TypeScript **kép ESM + CJS** có thể xuất bản với các khai báo kiểu (type declarations) được đóng gói, bản build `tsup` không cần cấu hình, và TypeScript được ghim ở bản `5.x` để nó build sạch trên cả CLI lẫn editor. Tạo ra `package.json`, `tsconfig.json`, cấu hình tsup, một smoke test, và các thiết lập `.vscode`, sau đó cài đặt, build, và xác minh.<br><br>→ [Tài liệu đầy đủ](../../skills/start-package/README.md) |
| **[skrapi](../../skills/skrapi/README.md)**               | _Start_ (Bắt đầu) — Trỏ nó vào một dự án mà bạn ngưỡng mộ và nó sẽ lập bản đồ cách codebase đó được xây dựng vào một thư mục `SKRAPI/` cố định chứa Markdown trọng tâm — kiến trúc, các phụ thuộc, và các prompt sẵn sàng để dán — để bạn có thể mượn các pattern phù hợp với dự án của riêng mình trước khi bắt đầu. Hoạt động trên mọi stack (web, mobile, extension, library, monorepo); mọi mô tả đều được xác minh dựa trên mã thực tế, không bao giờ đoán mò từ tên gói. Đầu ra đa ngôn ngữ (🇪🇸 ES · 🇺🇸 EN · 🇨🇳 ZH).<br><br>→ [Tài liệu đầy đủ](../../skills/skrapi/README.md) |
| **[end](../../skills/end/README.md)**                     | _End_ (Kết thúc) — Hiểu dự án của bạn từ đầu đến cuối. Cung cấp một chẩn đoán rõ ràng (các bug đã được xác nhận, rủi ro, cơ hội, nợ kỹ thuật) với các tham chiếu cụ thể, đề xuất hướng kiến trúc phù hợp cho codebase _này_, và xây dựng một kế hoạch thực thi có trật tự. Mỗi thay đổi diễn ra trong một giai đoạn cô lập, có thể xem xét lại — nó chỉ tiếp tục khi bạn nói `go`, `start`, hoặc `proceed`, và không có file nào bị động chạm trong quá trình phân tích.<br><br>→ [Tài liệu đầy đủ & ví dụ](../../skills/end/README.md) |

> **Lưu ý:** Mỗi skill đều đi kèm với một README chi tiết của riêng nó. Trang gốc đưa ra cái nhìn tổng quan ở mức cao; hãy đi sâu vào `./skills/<skill>/README.md` để biết cách sử dụng sâu hơn, xem các báo cáo ví dụ và các cam kết bảo đảm.

## Cài đặt

Mỗi skill được cài đặt theo cùng một cách — chọn cái bạn cần:

```bash
npx skills add bastndev/skills --skill start-package   # Start (Bắt đầu) — tạo cấu trúc gói TS npm
npx skills add bastndev/skills --skill skrapi          # Start (Bắt đầu) — nghiên cứu & tài liệu hóa bất kỳ codebase nào
npx skills add bastndev/skills --skill end             # End (Kết thúc) — kiểm toán & tái cấu trúc an toàn
```

## Cách Skill "End" Hoạt Động

`end` là skill trưởng thành nhất trong bộ công cụ. Đây là quy trình làm việc từ đầu đến cuối của nó:

1. **Phân tích trước tiên** — Lập bản đồ các điểm vào và hiểu dự án. **Không có file nào bị sửa đổi.**
2. **Báo cáo có cấu trúc** — Các phát hiện rõ ràng được phân thành Bugs (kèm theo mức độ nghiêm trọng), Nợ/Rủi ro và Đề xuất, cộng với tổng quan về tình trạng sức khỏe được chấm điểm, một đề xuất kiến trúc và một kế hoạch có trật tự — tất cả đều được hỗ trợ bởi các tham chiếu cụ thể đến từng dòng và file.
3. **Bạn ủy quyền từng giai đoạn** — Nó thực thi **chính xác một giai đoạn** tại một thời điểm. Sau mỗi giai đoạn, bạn nhận được một bản tóm tắt chính xác về các thay đổi, các xác minh đã thực hiện, và danh sách các giai đoạn còn lại.
4. **Kiểm soát toàn diện & an toàn** — Không bao giờ tạo test nếu dự án không có. Không bao giờ thêm dependency hoặc thay đổi trình quản lý gói mà không có sự cho phép. Tôn trọng công việc chưa được commit (uncommitted) của bạn và luôn giữ nguyên hành vi hiện tại trừ khi đang sửa một bug chính đáng.

Để xem quy trình làm việc đầy đủ, định dạng báo cáo chính xác (bao gồm các khối đóng bắt buộc), quy tắc quyết định kiến trúc và tất cả các đảm bảo an toàn, hãy đọc tài liệu skill dành riêng:

→ **[End – Tái Cấu Trúc Dự Án](../../skills/end/README.md)**

Đặc tả nội bộ đầy đủ nằm trong [skills/end/SKILL.md](../../skills/end/SKILL.md).

## Lộ Trình (Roadmap)

- **Start** (Bắt đầu) — `start-package` (tạo cấu trúc) và `skrapi` (nghiên cứu codebase hiện có) được phát hành hôm nay; nhiều công cụ tạo cấu trúc `start-*` khác đang trên đường ra mắt.
- **Middle** (Giữa) — các công cụ cải tiến theo yêu cầu, tập trung (hiệu suất, bảo mật, UX, xóa mã chết) đang được lên kế hoạch.
- **End** (Kết thúc) — `end` được phát hành hôm nay; nhiều runtime hơn, các chế độ tái cấu trúc chuyên biệt bổ sung và các tiện ích (utilities) đang được lên kế hoạch.

Mỗi skill đều đi kèm với tài liệu riêng (giống như [End – Tái Cấu Trúc Dự Án](../../skills/end/README.md) hiện tại).

---

<br>

<div align="center">
  <p align="center">
  <sub>Được xây dựng cho các nhà phát triển muốn các AI agent của họ hành động với kỷ luật của một kỹ sư senior.</sub>
</p>

_Nếu bạn tìm thấy bất kỳ lỗi nào hoặc có phản hồi, vui lòng [mở một issue](https://github.com/bastndev/skills/issues/new)._

<sub>Sản xuất tại 🇵🇪 bởi <a href="https://gohit.xyz">Gohit X</a> · Được cấp phép dưới <a href="https://github.com/bastndev/skills/blob/main/LICENSE">`MIT`</a></sub>

</div>
