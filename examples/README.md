# Aivis Cloud TTS Examples

This directory contains example configurations and usage patterns for the Aivis Cloud TTS skill.

## Files

- `config_example.json` - Sample configuration file with placeholder API key
- `sample_texts/` - Example text files for different use cases

## Quick Start

1. **Copy the example config**:
   ```bash
   cp examples/config_example.json config.json
   ```

2. **Edit `config.json`**:
   Replace `YOUR_API_KEY_HERE` with your actual Aivis Cloud API key from https://hub.aivis-project.com/cloud-api/dashboard

3. **Test basic TTS**:
   ```bash
   python scripts/tts.py --text "こんにちは、世界！" test.mp3
   ```

## Example Texts

### Simple Greeting (`simple_greeting.txt`)
Basic text-to-speech with default settings.

### Storytelling (`storytelling.txt`)
Longer text example demonstrating narrative capabilities.

### SSML Prosody (`ssml_prosody.txt`)
Example using SSML tags for speaking rate and pitch control.

### Technical Documentation (`technical_doc.txt`)
Example of technical content narration.

## Voice Model References

### まお (MAO)
- **UUID**: `a59cb814-0083-4369-8542-f51a29e72af7`
- **Styles**: ノーマル, ふつー, あまあま, おちつき, からかい, せつなめ
- **Best for**: Conversational content, tutorials, friendly narration

### コハク (KOHAKU)
- **UUID**: `22e8ed77-94fe-4ef2-871f-a86f94e9a579`
- **Styles**: ノーマル, あまあま, せつなめ, ねむたい
- **Best for**: Soft narration, bedtime stories, gentle explanations

## Output Format Guide

| Format | Use Case | File Size | Quality |
|--------|----------|-----------|---------|
| **mp3** | Web playback, podcasts | Small | Good |
| **flac** | Archives, high-quality storage | Medium | Excellent |
| **wav** | Editing, highest quality | Large | Lossless |
| **aac** | Mobile devices, streaming | Small | Good |
| **opus** | Low-bandwidth streaming | Smallest | Very Good |

## Common Workflows

### Generate Multiple Files
```bash
# Process all text files in a directory
for file in input/*.txt; do
    python scripts/tts.py "$file" "output/$(basename "$file" .txt).mp3"
done
```

### Create Different Styles
```bash
# Generate the same text in different styles
python scripts/tts.py --style "ノーマル" text.txt normal.mp3
python scripts/tts.py --style "からかい" text.txt teasing.mp3
python scripts/tts.py --style "あまあま" text.txt sweet.mp3
```

### Batch with Different Models
```bash
# Generate with different voice models
python scripts/tts.py --model "a59cb814-0083-4369-8542-f51a29e72af7" text.txt mao.mp3
python scripts/tts.py --model "22e8ed77-94fe-4ef2-871f-a86f94e9a579" text.txt kohaku.mp3
```

## Tips for Best Results

1. **Text Preparation**: Use proper punctuation and line breaks for natural pauses
2. **Character Limit**: Keep each request under 3,000 characters
3. **SSML**: Use SSML tags for precise control over prosody and timing
4. **Testing**: Test with short samples before processing large batches
5. **Quality**: Use FLAC for archival, MP3 for web distribution

## Troubleshooting

See the main SKILL.md for detailed troubleshooting information.

---

For more information, visit: https://api.aivis-project.com/v1/docs
