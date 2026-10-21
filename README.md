# 戳戳布偶｜21 段語音版

本版本保留原本布偶、文字／語音切換及音量調整功能。

## GitHub Pages

將 `index.html`、整個 `sounds/` 資料夾上傳至 GitHub Repository 根目錄，並部署 GitHub Pages。

### 管理語音檔

網頁會在載入時讀取 `sounds/manifest.json`，並從檔案清單中隨機選擇音效，不再要求使用 `sound_01` 等固定名稱。

**增加、刪除或更名語音**時，請同步更新清單：

1. 把 MP3 放到 `sounds/` 資料夾，或從資料夾移除舊檔。
2. 使用 Python 執行 `python update_sounds.py`，自動掃描資料夾、重新產生 `sounds/manifest.json`。
3. 將變更的音檔與 `sounds/manifest.json` 一起 Commit/Push。

不使用 Python 也可直接編輯 `sounds/manifest.json`：它是檔名字串組成的 JSON 陣列，必須與實際檔名一致。

**重要：** GitHub Pages 不支援直接列出資料夾中的檔案，所以只上傳新 MP3、卻不更新 manifest，網頁不會自動發現它。新清單會在下次重新載入網頁時生效。

## 本次更新

新增 7 個阿景語錄音檔，目前共 21 個 MP3。新音檔已使用響度標準化處理（目標 -18 LUFS，峰值 -2 dBTP），原 14 個音檔保留；manifest.json 已重新產生。
