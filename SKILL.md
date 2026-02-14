---
name: aivis-cloud-tts
description: Use this skill when the user wants to generate Japanese speech audio from text using Aivis Cloud API. Supports multiple voice models (まお, コハク) and audio formats (WAV, MP3, FLAC, AAC, Opus). Ideal for creating voiceovers, podcasts, or adding speech to applications.
---

# Aivis Cloud TTS Skill

## Goal

Generate high-quality Japanese speech audio from text using Aivis Cloud API. This skill provides fast, cloud-based text-to-speech synthesis with support for multiple character voices and audio formats.

## Instructions

### Prerequisites

1. **API Key Required**: You must have an Aivis Cloud API key.
   - Get one at: https://hub.aivis-project.com/cloud-api/dashboard
   - Save it in a local config file (see examples/config_example.json)

2. **Install Dependencies**:
   ```bash
   pip install requests
   ```

### Basic Usage

1. **Simple Text-to-Speech**:
   Run the TTS script with text directly:
   ```bash
   python scripts/tts.py --text "こんにちは、リリスです。" output.mp3
   ```

2. **From File**:
   Generate audio from a text file:
   ```bash
   python scripts/tts.py input.txt output.mp3
   ```

3. **With Style**:
   Use a specific speaking style:
   ```bash
   python scripts/tts.py --style "からかい" input.txt output.mp3
   ```

### Advanced Options

- **Output Format**: `--format {wav|flac|mp3|aac|opus}`
- **SSML Support**: `--ssml` (enable SSML parsing)
- **Custom Dictionary**: `--dictionary {uuid}`
- **Disable Normalizer**: `--no-normalizer`

### Available Voice Models

**まお (MAO)** - UUID: `a59cb814-0083-4369-8542-f51a29e72af7`
- Styles: ノーマル, ふつー, あまあま, おちつき, からかい, せつなめ

**コハク (KOHAKU)** - UUID: `22e8ed77-94fe-4ef2-871f-a86f94e9a579`
- Styles: ノーマル, あまあま, せつなめ, ねむたい

### Script Location

The TTS script is located at:
```
scripts/tts.py
```

### Configuration

Create a `config.json` file in the skill directory with your API key:

```json
{
  "api_key": "your_api_key_here",
  "default_model_uuid": "22e8ed77-94fe-4ef2-871f-a86f94e9a579",
  "default_style": "ノーマル",
  "default_format": "mp3",
  "use_ssml": false,
  "use_volume_normalizer": true
}
```

## Constraints

### ⚠️ IMPORTANT WARNINGS

1. **API Key Security**: NEVER commit API keys to version control. Always use environment variables or local config files.
2. **Character Limit**: Maximum 3,000 characters per request. For longer texts, split into chunks naturally.
3. **Rate Limiting**: If you receive HTTP 429, wait and retry.
4. **Credit Management**: Monitor your AivisHub dashboard for credit balance (Pay-as-you-go) or subscription status.

### ⛔ DO NOT

- Do NOT embed API keys in code or commit them
- Do NOT exceed 3,000 characters per single request
- Do NOT use the API for illegal or harmful content
- Do NOT distribute generated audio as your own voice

### ✅ DO

- Always validate text length before sending
- Use appropriate output formats (mp3 for web, flac for archives)
- Check credit balance before large batch jobs
- Use SSML for prosody control when needed

## Examples

### Example 1: Basic Greeting

**Input Text**:
```
こんにちは、リリスです。今日はいい天気ですね。
```

**Command**:
```bash
python scripts/tts.py --text "こんにちは、リリスです。今日はいい天気ですね。" greeting.mp3
```

**Output**: `greeting.mp3` (approximately 3-5 seconds, ~50-100KB)

### Example 2: Storytelling with Kohaku

**Input File** (`story.txt`):
```
昔々、あるところに小さな村がありました。村には優しい人々が住んでいて、
毎日楽しく過ごしていました。ある日、村の近くに魔法の森が現れました。
```

**Command**:
```bash
python scripts/tts.py --style "あまあま" story.txt story.mp3
```

**Output**: `story.mp3` (approximately 15-20 seconds, ~300-500KB)

### Example 3: SSML with Prosody Control

**Input SSML** (`ssml_input.txt`):
```xml
<speak>
  こんにちは。<break time="0.5s"/>
  <prosody rate="1.2" pitch="1.1">
    今日はいい天気ですね。
  </prosody>
  <break time="0.3s"/>
  散歩に行きましょう！
</speak>
```

**Command**:
```bash
python scripts/tts.py --ssml ssml_input.txt prosody.mp3
```

**Output**: `prosody.mp3` with controlled speaking rate and pitch

### Example 4: High-Quality Archive

**Command**:
```bash
python scripts/tts.py --format flac --style "せつなめ" narration.txt narration.flac
```

**Output**: `narration.flac` (lossless compression, smaller size than WAV)

## Troubleshooting

### Error: 401 Unauthorized
- **Cause**: Invalid API key
- **Fix**: Check your config.json and verify the API key in AivisHub dashboard

### Error: 402 Payment Required
- **Cause**: Insufficient credits
- **Fix**: Top up credits or switch to subscription plan at AivisHub

### Error: 429 Too Many Requests
- **Cause**: Rate limit exceeded
- **Fix**: Wait 30-60 seconds before retrying

### Error: Text Too Long
- **Cause**: Input exceeds 3,000 characters
- **Fix**: Split text into logical chunks (sentences, paragraphs) and process separately

## Related Resources

- **AivisHub**: https://hub.aivis-project.com
- **API Documentation**: https://api.aivis-project.com/v1/docs
- **Dashboard**: https://hub.aivis-project.com/cloud-api/dashboard
- **Pricing**: 10,000 characters for ¥440 (tax included) or ¥1,980/month unlimited

## Integration Tips

### For Antigravity Workflows

This skill can be combined with other skills in workflows:
- **Documentation Generation**: Use with markdown-to-pdf skills to create narrated guides
- **Content Creation**: Pair with web-scraping skills to narrate articles
- **Accessibility**: Generate audio descriptions for visually impaired users

### Batch Processing

For multiple files, use shell scripting:
```bash
for file in chapters/*.txt; do
    python scripts/tts.py "$file" "audio/$(basename $file .txt).mp3"
done
```

### Monitoring

After generation, check response headers:
- `X-Aivis-Billing-Mode`: PayAsYouGo or Subscription
- `X-Aivis-Character-Count`: Characters used
- `X-Aivis-Credits-Remaining`: Remaining credits

---

*This skill integrates Aivis Cloud API v1. Last updated: 2026-02-15*
