## install git in the system to download the repo
#!/bin/bash
sudo su
yum update -y
yum install -y git
exit

##create a virtual environment
python3 -m venv demo

##change folder to the virtual environment
cd demo

##Activate the virtual environment
source ~/demo/bin/activate

## clone the repo
git clone https://github.com/satishk01/LLMsample.git

##go to the folder /LLMsample/llama2
cd LLMsample
cd llama2


##download the model to the working folder
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin

##install the necessary packages
pip install -r requirements.txt

## create the index 
python3 ./genIndex.py

## run the bot
chainlit run ./app.py

Make sure the port 8000 is open in your security group . This is the port in which the app will communicate


