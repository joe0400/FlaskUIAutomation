

sudo apt-get install python3-pip
sudo apt-get install git git-lfs
sudo apt-get install portaudio19-dev
mkdir models
cd models
git lfs clone https://huggingface.co/huggyllama/llama-7b

cd ..
mkdir llama_cpp
cd llama_cpp
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
make -j $(nproc --all)


mkdir llama_model_server

pip3 install flask openai tacotron pyaudio transformers numpy librosa


