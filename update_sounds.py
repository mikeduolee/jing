#!/usr/bin/env python3
"""Regenerate sounds/manifest.json from audio files (run before committing)."""
from pathlib import Path
import json
folder=Path(__file__).resolve().parent/'sounds'
entries=sorted(p.name for p in folder.iterdir() if p.is_file() and p.suffix.lower() in {'.mp3','.ogg','.wav','.m4a'})
(folder/'manifest.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Updated manifest with {len(entries)} audio files')
