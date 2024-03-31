Hugging face cli installer

pip install -U "huggingface_hub[cli]"



Steps to download the models


7B
huggingface-cli download jartine/llava-v1.5-7B-GGUF llava-v1.5-7b-Q4_K.gguf --local-dir . --local-dir-use-symlinks False
huggingface-cli download jartine/llava-v1.5-7B-GGUF llava-v1.5-7b-mmproj-f16.gguf --local-dir . --local-dir-use-symlinks False

13B
huggingface-cli download PsiPi/liuhaotian_llava-v1.5-13b-GGUF llava-v1.5-13b-Q5_K_M.gguf --local-dir . --local-dir-use-symlinks False
huggingface-cli download PsiPi/liuhaotian_llava-v1.5-13b-GGUF mmproj-model-f16.gguf --local-dir . --local-dir-use-symlinks False



Steps to install llama-cpp

sudo yum install clang
pip install llama-cpp-python==0.2.55 --no-cache-dir

Other package installation

pip install pyyaml==6.0.1
pip install Pillow==10.2.0
pip install transformers==3.38.2
pip install torch==2.1
pip install scipy
pip install numpy




