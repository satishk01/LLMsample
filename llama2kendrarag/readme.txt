Steps to install

Create a virtual environment

python3 -m venv demo

Activate virtual environment and add the necessary packages

cd demo
source ~/demo/bin/activate

pip install langchain==0.0.279
pip install boto3>=1.28.27
pip install streamlit

create a folder images and move the image files from s3 bucket to the images folder.
The images are available in the Github

mkdir images
cd images
aws s3 cp s3://<<bucket_name>>/<<folder_name>>/user-icon.png ./
aws s3 cp s3://<<bucket_name>>/<<folder_name>>/ai-icon.png ./


Now let us go back to the demo folder and create three files. app.py, app_de.py  and kendra_chat_llama_2.py. These files are available in Github.

create the environment variables

export AWS_REGION="us-east-1"
export KENDRA_INDEX_ID="7d3d6bff-fea6-470b-a2ec-ac6d5ceb904f"
export LLAMA_2_ENDPOINT="meta-textgeneration-llama-2-7b-f-2024-05-04-05-24-54-650"

make the changes as per the AWS account region , kendra Index ID and sagemaker endpoint.


run these scripts in the demo folder

to start the normal english app run

streamlit run app.py llama2

to start the German app run

streamlit run app_de.py llama2

I have also uploaded the file "llama2textgen.ipynb" which has the code to generate the endpoint.

