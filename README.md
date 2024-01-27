---
title: LinguisticsChat
emoji: 🗣️
colorFrom: indigo
colorTo: blue
sdk: gradio
sdk_version: 4.8.0
app_file: main.py
pinned: false
license: gpl-3.0
---

# LinguisticsChat

LinguisticsChat is an advanced open-source chatbot platform tailored for individuals interested in exploring questions about the field of linguistics. It leverages the latest advancements from OpenAI's GPT-4 and a customized knowledge base to provide insightful and accurate responses. LinguisticsChat serves as a reliable resource for students, academics, and enthusiasts seeking to deepen their understanding of linguistic concepts.

## Features

- **Linguistic Expertise**: Gain insights into the field of linguistics with targeted responses from an AI trained on a specialized knowledge base.
- **Customized Knowledge Retrieval**: Uses a bespoke Vector Store from `langchain_community.vectorstores` to pull relevant information from a ChromaDB-backed persistent storage.
- **Advanced GPT-4 Interaction**: Interface with OpenAI's latest GPT-4 model for nuanced and in-depth conversation.
- **Secure Access**: Protected with a passcode to ensure controlled usage.

## How It Works

LinguisticsChat incorporates the `langchain` library to forge a powerful QA chain with a custom `ChatOpenAI` instance that utilizes OpenAI's GPT-4 model. The process involves users asking questions about linguistics, and the system intelligently retrieves knowledge from its database before generating an informed response. The chatbot is designed to simulate an expert-level conversation, drawing from both its knowledge base and the linguistic prowess of GPT-4.

## Getting Started

### Prerequisites

Before running LinguisticsChat, ensure that you have the following prerequisites installed:
- Python 3.8 or later
- Pipenv or another Python package manager

### Installation

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies using Pipenv or pip:

   ```
   pipenv install
   ```
   or
   ```
   pip install -r requirements.txt
   ```

4. Generate a `.env` file in the root directory, placing your `OPENAI_API_KEY` and `PASSCODE_KEY` within it.

### Running LinguisticsChat

To start the application, navigate to the project directory and run:

```
python main.py
```

The interface will be launched in your default web browser, or you can access it at the URL provided in the terminal.

## Contributing

Contributions to LinguisticsChat are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

LinguisticsChat is licensed under the *GPL-3.0 license* - see the `LICENSE` file for details.

## Acknowledgments

- The developers at OpenAI for their groundbreaking GPT-4 language model.
- The `gradio` team for the library that allows for swift ML model interface development.
- The creators of `langchain` for facilitating easy integration of AI language models.

Your engagement with LinguisticsChat is highly valued. We hope it serves your curiosity well and becomes a staple tool in your linguistic endeavors.
