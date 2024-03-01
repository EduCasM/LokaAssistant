from langchain.retrievers import AmazonKendraRetriever
from langchain.chains import RetrievalQA
from langchain import OpenAI
from langchain.prompts import PromptTemplate
import os


def build_chain():
  region = os.environ["AWS_REGION"]
  kendra_index_id = os.environ["KENDRA_INDEX_ID"]

  llm = OpenAI(batch_size=5, temperature=0, max_tokens=300)

  retriever = AmazonKendraRetriever(index_id=kendra_index_id,region_name=region)

  prompt_template = """
  The following is a friendly conversation between a human and an AI assistant. 
  The Loka assistant is talkative and provides lots of specific details from its context 
  (AWS SageMaker documentation).
  If the assistant does not know the answer to a question, it truthfully says it 
  does not know.
  {context}
  Instruction: Based on the above documents, provide a detailed answer for, {question} Answer "don't know" 
  if not present in the document. 
  Solution:"""
  PROMPT = PromptTemplate(
      template=prompt_template, input_variables=["context", "question"]
  )
  chain_type_kwargs = {"prompt": PROMPT}
    
  return RetrievalQA.from_chain_type(
      llm, 
      chain_type="stuff", 
      retriever=retriever, 
      chain_type_kwargs=chain_type_kwargs, 
      return_source_documents=True
  )

def run_chain(chain, prompt: str, history=[]):
    result = chain(prompt)
    # To make it compatible with chat samples
    return {
        "answer": result['result'],
        "source_documents": result['source_documents']
    }

if __name__ == "__main__":
    questions = ["What's SageMaker?", "What are all AWS regions where SageMaker is available?", "How to check if an endpoint is KMS encrypted?",
                "What are SageMaker Geospatial capabilities?"]
    
    for question in questions:
        chain = build_chain()
        result = run_chain(chain, question)
        print(result['answer'])
      
    if 'source_documents' in result:
        print('Sources:')
        for d in result['source_documents']:
          print(d.metadata['source'])
