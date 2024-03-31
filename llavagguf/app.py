#### This was a sample code built. Can be improved further

import streamlit as st
from llama_cpp import Llama
from llama_cpp.llama_chat_format import Llava15ChatHandler
from PIL import Image
from io import BytesIO
import base64
import sys
import os




# App title
st.set_page_config(page_title="LLava MultiModal Chatbot")


model_file = "llava-v1.5-7b-Q4_K.gguf"
model_mmproj_file = "llava-v1.5-7b-mmproj-f16.gguf"
chat_handler = Llava15ChatHandler(clip_model_path=model_mmproj_file)
model = Llama(
        model_path=model_file,
        chat_handler=chat_handler,
        n_ctx=2048,
        n_gpu_layers=-1,  # Set to 0 if you don't have a GPU
        verbose=True,
        logits_all=True,
    )

def save_uploadedfile(uploadedfile):
     if uploadedfile != None:
       with open(os.path.join("images",uploadedfile.name),"wb") as f:
           f.write(uploadedfile.getbuffer())
       im = Image.open('./images/'+uploadedfile.name)
       rgb_im = im.convert("RGB")
       file_path = 'C:/demo/'+uploadedfile.name
       file_path_components = file_path.split('/')
       file_name_and_extension = file_path_components[-1].rsplit('.', 1)
       finalFileName = file_name_and_extension[0]+".jpg"
       rgb_im.save('./images/'+finalFileName)
       modifiedfile = './images/'+finalFileName
       return modifiedfile



def image_b64encode(img: Image) -> str:
    """ Convert image to a base64 format """
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")




with st.sidebar:
    st.title('Llava MultiModal Chatbot')
    selected_model = st.sidebar.selectbox('Choose a LLava model', ['llava-v1.5-7B', 'liuhaotian_llava-v1.5-13b'] , key='selected_model')
    if selected_model == 'liuhaotian_llava-v1.5-13b':
      print('Selected Model is ',selected_model)
    elif selected_model == 'llava-v1.5-7B':
      print('Selected Model is ',selected_model)
    

#    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
#    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
#    max_length = st.sidebar.slider('max_length', min_value=64, max_value=4096, value=512, step=8)

    st.markdown('?? Learn how to build this app !')



# Function to generate llava response
def generate_llava_response(prompt_input):
    """ Ask model a question """

    file_path = 'C:/demo/'+uploaded_file.name
    file_path_components = file_path.split('/')
    file_name_and_extension = file_path_components[-1].rsplit('.', 1)
    finalFileName = file_name_and_extension[0]+".jpg"
    img = Image.open('./images/'+finalFileName)
    image_b64 = image_b64encode(img)
    out_stream = model.create_chat_completion(
      messages = [
          {
              "role": "system",
              "content": "MultiModal AI assistant to describes images."
          },
          {
              "role": "user",
              "content": [
                  {"type": "image_url",
                   "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}},
                  {"type" : "text",
                   "text": prompt}
              ]
          }
      ],
      stream=True,
      temperature=0.2
    )


    # Get characters from stream
    output = ""
    for r in out_stream:
        data = r["choices"][0]["delta"]
        if "content" in data:
            print(data["content"], end="")
            sys.stdout.flush()
            output += data["content"]

    return output

if selected_model == 'liuhaotian_llava-v1.5-13b':
    print('liuhaotian_llava-v1.5-13b Model is Selected , the code needs to be written for this ')
elif selected_model == 'llava-v1.5-7B':
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    save_uploadedfile(uploaded_file)


    # Ensure session state for messages if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "LLAVA Based MultiModel AI Bot for assistance?"}]

    # Display or clear chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message.get("type") == "image":
                st.image(message["content"])
            else:
                st.write(message["content"])

    
    # Sidebar to clear chat history
    def clear_chat_history():
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

    st.sidebar.button('Switch LLAVA Model', on_click=clear_chat_history)
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    # Text input for chat
    prompt = st.text_input("Type a message:")

    # Button to send the message/image
    if st.button('Send'):
        if uploaded_file:
            # If an image is uploaded, store it in session_state
            st.session_state.messages.append({"role": "user", "content": uploaded_file, "type": "image"})

        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate a new response if the last message is not from the assistant
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = generate_llava_response(prompt)
                    placeholder = st.empty()
                    full_response = ''
                    for item in response:
                        full_response += item
                        placeholder.markdown(full_response)
                    placeholder.markdown(full_response)
            message = {"role": "assistant", "content": full_response}
            st.session_state.messages.append(message)
