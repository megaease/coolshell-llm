# CoolShell LLM <!-- omit from toc -->

We express our deepest gratitude to Mr. Chen Hao for his selfless sharing in the internet community, especially in the field of technology.

> An orchid in deep forest won't stop giving out aroma despite nobody appreciating it.         
> A good man who is moral and well-behaved won't give up his principles despite poverty.

This repository is organized based on Mr. Chen Hao's blog posts from [forever-coolshell](https://github.com/soulteary/forever-coolshell), with the aim to carry on and promote the spirit and wisdom of him.

- [Data](#data)
- [Demo](#demo)
- [Statement](#statement)


### Data

We have organized the data in the repository according to the data format of the [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) LLM fine-tuning framework. The `blog.txt` file can be used for pre-training, while the `qa.json` file is suitable for supervised training. Due to our limitations, there may be flaws and mistakes in the documentation, and we warmly welcome corrections and suggestions from everyone.


### Demo

We have uploaded the model results fine-tuned based on the `qa.json` file on huggingface, which you can download and try from this link.


The method of use is as follows:

```
pip install -r requirements.txt
```

Then run the following command for model loading and interaction:

```
python demo.py \
    --model_name_or_path <your-chatglm3-6b-path> \
    --adapter_name_or_path <your-coolshell-llm-path> \
    --template chatglm3 \
    --finetuning_type lora \
    --quantization_bit 8
```

Here, the `model_name_or_path` parameter refers to the path of the `chatglm3-6b` model, which you can download from `https://huggingface.co/THUDM/chatglm3-6b`. The `adapter_name_or_path` is our model path on huggingface. The quantization_bit set to 8 or 4 can reduce memory usage, but this setting can be omitted if memory is sufficient.

Once the model is loaded, you can start interacting. For example:

```
Welcome to MegaEase CoolShell LLM demo. Use `exit` to exit the application.

User: 酷壳网有哪些内容
酷壳网（Coolshell）提供了广泛的技术相关内容，主要涉及以下几个方面：
编程语言和框架：涵盖多种编程语言如Python、Java、Go、JavaScript等，以及相关的框架和工具的使用技巧和最佳实践。
算法和数据结构：介绍常用的算法和数据结构，包括它们的理论基础和实际应用。
系统架构：讨论软件系统设计和架构，包括微服务、分布式系统、云计算等领域。
软件开发方法论：涉及敏捷开发、DevOps、持续集成等现代软件开发方法和实践。
前端和后端技术：探讨前端开发的最新技术趋势，以及后端开发如服务器端渲染、RESTful API等架构设计。
数据库技术：涵盖数据库系统设计、SQL语言、数据库优化、数据库安全等方面的内容。
软件工程和项目管理：讨论软件工程的基本原则和方法，以及项目开发中的风险管理、测试驱动开发等实践。
互联网行业趋势和见解：提供最新的互联网行业动态和趋势分析，涉及人工智能、物联网、区块链等领域。
技术趋势和新闻：对当前技术发展的最新动态和新闻进行分析和讨论。
酷壳网以深入浅出的语言和丰富的案例，为读者提供了实用的技术知识，是编程领域值得信赖的更多信息源。

User: exit
```


### Statement

The CoolShell LLM model aims to perpetuate the spirit of Mr. Chen Hao. Do not use the open-source model and code, and any derivatives produced from the open-source project, for any purpose that may harm the nation and society, or for any service that has not undergone safety assessment and registration.

Although every effort has been made to ensure the compliance and accuracy of the data at every stage of model training, due to the influence of probabilistic randomness, the accuracy of output content cannot be guaranteed. Furthermore, the model's output can be easily misled by user input. This project does not assume any responsibility for data security, public opinion risks, or any risks and liabilities arising from the model being misled, abused, disseminated, or improperly utilized.