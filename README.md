# 戳戳布偶｜漫畫互動遊戲

可直接部署在 GitHub Pages 的靜態單頁遊戲；不需要伺服器、建置工具或額外圖片檔。

## 功能

- 滑鼠食指指標、布偶局部按壓形變及回彈
- 28 句語錄隨機出現，避免連續相同
- 漫畫對話框、依語錄語氣變化的字級與色彩
- 對話框尾巴指向被戳部位
- 顯示約 4 秒（最後 0.4 秒淡出）；再次按壓立即更換
- 支援手機觸控與桌面瀏覽器

## GitHub Pages 上線步驟

1. 在 GitHub 建立一個 **Public** Repository（例如 `poke-doll`）。
2. 將本資料夾的 `index.html` 上傳至 Repository **根目錄**，再 Commit。
3. Repository → **Settings** → **Pages**。
4. 在 **Build and deployment** 設定 Source 為 **Deploy from a branch**，Branch 選 **main**、Folder 選 **/(root)**，按 **Save**。
5. 網站部署完成後，網址通常是 `https://<GitHub帳號>.github.io/poke-doll/`。

> 本頁使用 WebGL。若裝置停用 WebGL，布偶仍可顯示，但局部按壓形變可能無法使用。
