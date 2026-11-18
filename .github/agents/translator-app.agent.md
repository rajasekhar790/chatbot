---
name: Translator App
description: Maintain the Gradio English-to-French translation app and its LangChain/OpenAI integration.
---

Focus on the translator application in `app.py` and its Python dependencies in `requirements.txt`.

- Preserve the English-to-French workflow and the Gradio interface unless the request explicitly changes product behavior.
- Keep changes compatible with the Python version in `dockerfile` and with the dependency versions declared in `requirements.txt`.
- Read the OpenAI credential from the `OPENAI_API_KEY` environment variable; never hardcode, print, or commit credentials.
- Keep the translation function and Gradio interface aligned when changing inputs, outputs, or model behavior.
- Validate changes with focused checks and run the app only when the required environment variables and dependencies are available.
