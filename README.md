# 戳戳布偶 — GitHub Pages 26 段語音版

包含原本 21 段語音及新加入的 5 段 MP3，共 26 段。

部署：將 `index.html` 與整個 `sounds/` 資料夾上傳到 GitHub Pages 專案根目錄；不要只上傳 HTML。

語音清單：`sounds/manifest.json`，網頁將由清單載入 MP3 並隨機播放。

新音檔使用 ffmpeg 響度標準化，目標 -18 LUFS，峰值 -2 dBTP，其他網頁設定不變。
