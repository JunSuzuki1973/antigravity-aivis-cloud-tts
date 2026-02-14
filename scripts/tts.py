#!/usr/bin/env python3
"""
Aivis Cloud API - Text-to-Speech Generator
"""

import requests
import json
import argparse
import os
import sys
import re
from pathlib import Path

# スクリプトのディレクトリ
SCRIPT_DIR = Path(__file__).parent
CONFIG_FILE = SCRIPT_DIR / "config.json"

# デフォルト設定
DEFAULT_CONFIG = {
    "api_key": "",
    "default_model_uuid": "a59cb814-0083-4369-8542-f51a29e72af7",  # まお
    "default_style": "ノーマル",
    "default_format": "mp3",
    "use_ssml": False,
    "use_volume_normalizer": True
}

# APIエンドポイント
TTS_URL = "https://api.aivis-project.com/v1/tts/synthesize"

def load_config():
    """設定ファイルを読み込む"""
    if not CONFIG_FILE.exists():
        print(f"Error: Config file not found: {CONFIG_FILE}")
        print(f"Run setup.sh first to create config.json")
        sys.exit(1)

    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # デフォルト値とマージ
    config = {**DEFAULT_CONFIG, **config}

    return config

def clean_text(text):
    """
    テキストをクリーニング
    """
    # マークダウンの見出し記号削除
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    # 連続する空白をまとめる
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def generate_tts(config, text, output_path, style=None, output_format=None,
                 use_ssml=None, use_volume_normalizer=None, dictionary_uuid=None):
    """
    Aivis Cloud APIで音声生成
    """
    # テキストをクリーニング（SSML無効の場合のみ）
    if not use_ssml:
        text = clean_text(text)

    print(f"Text length: {len(text)} characters")

    # リクエストボディ
    payload = {
        "model_uuid": config["default_model_uuid"],
        "text": text,
        "use_ssml": use_ssml,
        "use_volume_normalizer": use_volume_normalizer,
        "output_format": output_format
    }

    # スタイル指定（style_nameまたはstyle_id）
    if style:
        # スタイルIDが数字ならstyle_idとして扱う
        if style.isdigit():
            payload["style_id"] = int(style)
        else:
            payload["style_name"] = style

    # ユーザー辞書指定
    if dictionary_uuid:
        payload["user_dictionary_uuid"] = dictionary_uuid

    # ヘッダー
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }

    print(f"Sending request to Aivis Cloud API...")
    print(f"  Model: {config['default_model_uuid']}")
    if style:
        print(f"  Style: {style}")
    print(f"  Format: {output_format}")
    print(f"  SSML: {use_ssml}")

    # リクエスト送信
    try:
        response = requests.post(TTS_URL, json=payload, headers=headers, timeout=120)
    except requests.exceptions.Timeout:
        print(f"Error: Request timed out (120s)")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code}")
        print(f"Response: {response.text}")
        return False

    # レスポンスヘッダー表示
    print("\nResponse Headers:")
    for key in ['X-Aivis-Billing-Mode', 'X-Aivis-Character-Count',
                'X-Aivis-Credits-Used', 'X-Aivis-Credits-Remaining']:
        if key in response.headers:
            print(f"  {key}: {response.headers[key]}")

    # 音声データを保存
    with open(output_path, 'wb') as f:
        f.write(response.content)

    print(f"\n✓ Audio saved to {output_path}")
    print(f"  Size: {len(response.content):,} bytes ({len(response.content)/1024:.2f} KB)")

    return True

def main():
    parser = argparse.ArgumentParser(description='Aivis Cloud API TTS Generator')
    parser.add_argument('input', nargs='?', help='Input file or use --text')
    parser.add_argument('output', help='Output audio file')
    parser.add_argument('--text', help='Input text directly (instead of file)')
    parser.add_argument('--style', help='Style name or ID (e.g., ノーマル, からかい)')
    parser.add_argument('--format', choices=['wav', 'flac', 'mp3', 'aac', 'opus'],
                        help='Output format (default: from config)')
    parser.add_argument('--ssml', action='store_true',
                        help='Enable SSML parsing')
    parser.add_argument('--no-normalizer', action='store_true',
                        help='Disable volume normalizer')
    parser.add_argument('--dictionary', help='User dictionary UUID')

    args = parser.parse_args()

    # 設定読み込み
    config = load_config()

    # テキストの取得
    if args.text:
        text = args.text
    elif args.input:
        with open(args.input, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        parser.print_help()
        print("\nError: Either input file or --text is required")
        sys.exit(1)

    # パラメータの決定
    style = args.style or config["default_style"]
    output_format = args.format or config["default_format"]
    use_ssml = args.ssml if args.ssml is not None else config["use_ssml"]
    use_volume_normalizer = not args.no_normalizer if args.no_normalizer else config["use_volume_normalizer"]

    # TTS生成
    success = generate_tts(
        config=config,
        text=text,
        output_path=args.output,
        style=style,
        output_format=output_format,
        use_ssml=use_ssml,
        use_volume_normalizer=use_volume_normalizer,
        dictionary_uuid=args.dictionary
    )

    if success:
        print("\n✅ TTS generation completed successfully!")
        sys.exit(0)
    else:
        print("\n❌ TTS generation failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
