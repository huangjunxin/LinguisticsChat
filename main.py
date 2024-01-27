import os
import time
import gradio as gr
import chromadb
import langchain
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.schema import SystemMessage
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from utils import system_message, human_template
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")
passcode_key = os.getenv("PASSCODE_KEY")

# Set LangChain Verbosity
langchain.verbose = True

# Define the ChatOpenAI model
llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key, model='gpt-4-0125-preview')

# Define the Embedding model
embedding = OpenAIEmbeddings()

# Load the knowledge base
persist_directory = 'chroma_db'
persist_client = chromadb.PersistentClient(path=persist_directory)
langchain_chroma = Chroma(
    client=persist_client,
    embedding_function=embedding,
)

# Define the custom prompt template
messages = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=system_message),
        HumanMessagePromptTemplate.from_template(human_template)
    ]
)

# Define the customized QA chain
qa_chain_custom = RetrievalQA.from_chain_type(
    llm,
    retriever=langchain_chroma.as_retriever(search_kwargs={"k": 3}),
    chain_type="stuff",
    return_source_documents=True,
    chain_type_kwargs={"prompt": messages}
)


def stream_response(response):
    for i in range(len(response)):
        time.sleep(0.01)
        yield response[: i + 1]


def assistant(message, history, passcode):
    print(message)
    print(history)

    if passcode != passcode_key:
        return "Please enter the correct passcode."

    res = qa_chain_custom.invoke(message)
    output = res["result"]
    return output


main_interface = gr.ChatInterface(
            fn=assistant,
            title="LinguisticsChat",
            description="Please enter the question you would like to ask about the field of linguistics.",
            retry_btn=None,
            undo_btn=None,
            additional_inputs=[
                gr.Textbox(
                    label="Passcode",
                    placeholder="You are required to enter the passcode to use this chatbot.",
                    type="password",
                    lines=1,
                    max_lines=1
                )
            ],
            additional_inputs_accordion=gr.Accordion(
                label="Passcode",
                open=True,
            )
        ).queue()


if __name__ == '__main__':
    main_interface.launch(show_api=False)
