#!/usr/bin/env python3
"""Generate a searchable, *unverified* OCR index from supplied screenshots."""
import argparse
import hashlib
from pathlib import Path
from rapidocr_onnxruntime import RapidOCR


def main():
    p = argparse.ArgumentParser()
    p.add_argument('screenshots', type=Path)
    p.add_argument('--output', type=Path, default=Path('docs/screenshot-ocr.md'))
    args = p.parse_args()
    files = sorted(args.screenshots.glob('*.jpg'))
    if not files:
        p.error('No JPG screenshots found')
    engine = RapidOCR()
    out = ['# Скриншоты: машинный OCR-индекс', '',
           'Это автоматическое распознавание, **не проверенная транскрипция**. Возможны пропуски, неверные цифры, знаки, порядок и объединение строк; низкая уверенность не выявляет всех ошибок. Сверяйте с JPEG. Текст описывает заявления автора, а не доказанную реализацию; версия страницы не установлена. Интерфейс и перекрытые части могут попасть в вывод. Хэши позволяют идентифицировать оригиналы из пользовательской папки Google Диска.', '']
    for file in files:
        print(file.name, flush=True)
        lines, _ = engine(str(file))
        out += [f'## {file.name}', '', f'SHA-256: `{hashlib.sha256(file.read_bytes()).hexdigest()}`', '', '```text']
        out += [f'{score:.3f}  {text}' for _, text, score in (lines or [])]
        out += ['```', '']
    args.output.write_text('\n'.join(out), encoding='utf-8')


if __name__ == '__main__':
    main()
