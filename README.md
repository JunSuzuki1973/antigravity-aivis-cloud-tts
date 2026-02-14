# Aivis Cloud TTS Skill for Antigravity

A Google Antigravity skill for generating high-quality Japanese speech audio using Aivis Cloud API.

## Overview

This skill provides fast, cloud-based text-to-speech synthesis with support for multiple character voices (まお, コハク) and audio formats (WAV, MP3, FLAC, AAC, Opus). Perfect for creating voiceovers, podcasts, or adding speech to applications.

## Features

- 🚀 **Fast Generation**: Start audio generation in as fast as 0.3 seconds
- 🎭 **Multiple Voices**: まお (MAO) and コハク (KOHAKU) with various speaking styles
- 📝 **Long Text Support**: Up to 3,000 characters per request
- 🎵 **Multiple Formats**: WAV, MP3, FLAC, AAC, Opus
- 🎚️ **SSML Support**: Control speaking rate, pitch, and volume
- 💰 **Flexible Pricing**: Pay-as-you-go or subscription options

## Quick Start

### 1. Get API Key

Visit [AivisHub](https://hub.aivis-project.com/cloud-api/dashboard) to get your API key.

### 2. Configure

Copy the example config and add your API key:
```bash
cp examples/config_example.json config.json
# Edit config.json and replace YOUR_API_KEY_HERE
```

### 3. Generate Audio

```bash
# Basic usage
python scripts/tts.py --text "こんにちは、世界！" output.mp3

# From file
python scripts/tts.py input.txt output.mp3

# With style
python scripts/tts.py --style "からかい" input.txt output.mp3
```

## Voice Models

### まお (MAO)
- **UUID**: `a59cb814-0083-4369-8542-f51a29e72af7`
- **Styles**: ノーマル, ふつー, あまあま, おちつき, からかい, せつなめ
- **Best For**: Conversational content, tutorials, friendly narration

### コハク (KOHAKU)
- **UUID**: `22e8ed77-94fe-4ef2-871f-a86f94e9a579`
- **Styles**: ノーマル, あまあま, せつなめ, ねむたい
- **Best For**: Soft narration, bedtime stories, gentle explanations

## Directory Structure

```
aivis-cloud-tts/
├── SKILL.md                      # Main skill definition (read by Antigravity)
├── README.md                     # This file
├── scripts/
│   └── tts.py                    # TTS generation script
├── examples/
│   ├── README.md                 # Usage examples
│   ├── config_example.json       # Configuration template
│   └── sample_texts/             # Sample text files
│       ├── simple_greeting.txt
│       ├── storytelling.txt
│       └── ssml_prosody.txt
└── config.json                   # Your local configuration (create this)
```

## Installation

This skill is installed at:
```
~/.gemini/antigravity/skills/aivis-cloud-tts/
```

It will be automatically discovered by Antigravity.

## Requirements

- Python 3.7+
- requests library: `pip install requests`

## Pricing

- **Pay-as-you-go**: ¥440 per 10,000 characters (tax included)
- **Subscription**: ¥1,980/month for unlimited usage (tax included)
- **Free Credits**: 500 credits (~11,000 characters) for new registrations

## Documentation

- **AivisHub**: https://hub.aivis-project.com
- **API Docs**: https://api.aivis-project.com/v1/docs
- **Dashboard**: https://hub.aivis-project.com/cloud-api/dashboard

## License

This skill is MIT licensed. Aivis Cloud API usage follows the [Aivis Project Terms of Service](https://aivis-project.com/terms).

## Credits

- Aivis Project: https://aivis-project.com/
- Aivis Cloud API: https://api.aivis-project.com/v1

---

**Created for Antigravity by Jun Suzuki** | Last updated: 2026-02-15
