
##create a virtual environment
pytnon3 -m venv demo

##change folder to the virtual environment
cd demo

##Activate the virtual environment
source ~/demo/bin/activate

##download the model to the demo folder
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin

##install the necessary packages
pip install -r requirements.txt

## run the bot
chainlit run ./app.py

Make sure the port 8000 is open in your security group . This is the port in which the app will communicate


