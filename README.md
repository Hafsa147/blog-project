# AI-Powered Blog Generator

A Python command-line tool that generates blog-style paragraphs from user-provided topics using the OpenAI API.

## What it does

1. Prompts the user for a topic.
2. Sends the topic to OpenAI's completion API with a fixed instruction prompt ("Write a paragraph on the following topic...").
3. Returns and prints the generated paragraph.
4. Loops, letting the user generate as many paragraphs as they want in one session until they choose to stop.

## Tech stack

- Python
- OpenAI API (`gpt-3.5-turbo-instruct`)
- `python-dotenv` for loading the API key from a local `.env` file

## Design decisions worth noting

- **API key handling**: the key is loaded from a `.env` file via `dotenv_values` rather than hardcoded into the script, keeping credentials out of source control (see Setup below for the `.gitignore` note).
- **Low temperature (0.3)**: intentionally set low rather than high. For a blog generator, more consistent and on-topic output is preferable to highly random, unpredictable variations between runs — this keeps generated paragraphs coherent and focused on the given topic.
- **Simple loop-based CLI**: rather than a one-shot script, the program keeps prompting the user in a loop so multiple paragraphs can be generated in a single session without restarting the program.

## Setup

1. Install dependencies:
   ```bash
   pip3 install openai python-dotenv
   ```
2. Create a `.env` file in the project root with your OpenAI API key:
   ```
   API_KEY=your-key-here
   ```
   Make sure `.env` is listed in `.gitignore` so your key is never committed.
3. Run it:
   ```bash
   python3 main.py
   ```
4. Follow the prompts to generate paragraphs on any topic, and enter anything other than `Y` when asked to stop.