# CoolShell LLM

感恩陈皓先生对中文互联网，尤其是技术领域无私的分享。

本仓库是根据 [forever-coolshell](https://github.com/soulteary/forever-coolshell) 中的博文进行一些处理，并通过对一些 LLM 大模型的 finetune，使这些大模型具有一些对互联网计算机领域的深刻见解。

使用时，请运行：
```
git clone https://github.com/megaease/coolshell-llm
cd coolshell-llm

pip3 install -r requirements.txt
python3 process.py <dir>/forever-coolshell
```
产生的 `blog.txt` 文件，在 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory/) 中作为预训练。