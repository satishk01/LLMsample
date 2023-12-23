from langchain import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
import chainlit as ct
import time
import asyncio

DB_FAISS_PATH = 'faiss-index-demo'

custom_prompt_template = """answer the user's question. if no data found return I dont know answer, try asking relavent question.

Context: {context}
Question: {question}

Answer to the question asked .
answer:
"""

def create_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])
    return prompt

#Retrieval chain
def get_response_from_qa_chain(llm, prompt, db):
    retrieval_chain = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                       retriever=db.as_retriever(search_kwargs={'k': 2}),
                                       return_source_documents=True,
                                       chain_type_kwargs={'prompt': prompt}
                                       )
    return retrieval_chain

#Loading the local model intoo llm
def load_llama2_llm():
    # Load the model llama-2-7b-chat.ggmlv3.q8_0.bin locally downloaded model here
    llm = CTransformers(
        model = "llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        max_new_tokens = 512,
        temperature = 0.5
    )
    return llm

#Answering bot creation
def answering_bot():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    llm = load_llama2_llm()
    qa_prompt = create_prompt()
    response = get_response_from_qa_chain(llm, qa_prompt, db)

    return response

#display result of the question asked
def final_result(query):
    bot_result = answering_bot()
    bot_response = bot_result({'query': query})
    return bot_response

#chainlit code
@ct.on_chat_start
async def start():
    chain = answering_bot()
    msg = ct.Message(content="The bot is getting initialized, please wait ...")
    await msg.send()
    msg.content = "Q&A bot is ready . Ask questions on the documents indexed?"
    await msg.update()

    ct.user_session.set("chain", chain)

@ct.on_message
async def main(message):
    chain = ct.user_session.get("chain") 
    cb = ct.AsyncLangchainCallbackHandler(
        stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
    )
    cb.answer_reached = True
    res = await chain.acall(message.content, callbacks=[cb])
    answer = res["result"]
    
    await ct.Message(content=answer).send()

