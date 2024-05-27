Steps to install

Create a virtual environment

python3 -m venv demo

Activate virtual environment and add the necessary packages

cd demo
source ~/demo/bin/activate


copy the files app.py, kendra_bedrock_query.py, .env and requirements.txt to this folder.

Install the necessary packages by running the command

pip install -r requirements.txt

In the file .env set proper value for Kendra_index and REGION . Plese amake it as per the setup done. The below are sample values that needs to be changed.

kendra_index=7a4b17ac-2f94-1234-5678-f0ceefdf0661
REGION=us-east-1

run these scripts in the demo folder

to start the normal english app run

streamlit run app.py

