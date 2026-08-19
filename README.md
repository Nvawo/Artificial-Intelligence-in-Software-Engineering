# AI: Scaffolding a Robust API Integration

## Overview
Refactored `sentiment_analyzer.py` to support secure environment-variable authentication and granular exception handling using contextual AI prompting.

## Files Included
- `sentiment_analyzer.py`: Initial Python script.
- `sentiment_analyzer_refactored.py`: Refactored script containing secure header injection and specific error catching (`Timeout`, `ConnectionError`).
- `README.md`: Task documentation.

## How to Run
```bash
export TEXT_PROCESSING_API_KEY="DUMMY_KEY"
python3 sentiment_analyzer_refactored.py "This assignment setup is clear!"
