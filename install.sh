

sudo apt-get install python3-pip
sudo apt-get install git git-lfs
sudo apt-get install portaudio19-dev
mkdir models
cd models
git lfs clone https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF

cd ..
mkdir llama_cpp
cd llama_cpp
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
make -j $(nproc --all)


mkdir llama_model_server

pip3 install flask openai tacotron pyaudio transformers numpy librosa


