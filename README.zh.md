# CoolShell LLM <!-- omit from toc -->

\[ [English](./README.md) | 中文 \]


感恩陈皓先生对中文互联网，尤其是技术领域无私的分享。

> 芝兰生于深谷，不以无人而不芳。   
> 君子修身养德，不以穷困而改志。

本仓库是根据 [forever-coolshell](https://github.com/soulteary/forever-coolshell) 中陈皓先生的博文整理而成，希望借此传承发扬陈皓先生的精神与智慧。

- [数据](#数据)
- [演示示例](#演示示例)
- [声明](#声明)


### 数据

我们根据 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) LLM 微调框架的数据格式，认真整理了仓库内的数据。其中，`blog.txt` 文件可用于预训练，而 `qa.json` 文件则适用于监督式训练。由于能力所限，文档中的缺陷和错误在所难免，我们衷心欢迎大家的指正和建议。


### 演示示例

我们已经在 huggingface 上载了基于 `qa.json` 文件微调得到的模型结果，你可以在此[地址](https://huggingface.co/zhaokun/coolshell-llm)下载试用。

试用方法如下：
```
pip install -r requirements.txt
```

然后运行以下命令进行模型加载和交互：
```
python demo.py \
    --model_name_or_path <your-chatglm3-6b-path> \
    --adapter_name_or_path <your-coolshell-llm-path> \
    --template chatglm3 \
    --finetuning_type lora \
    --quantization_bit 8
```

其中，`model_name_or_path` 参数指的是 chatglm3-6b 模型的路径，你可以从 `https://huggingface.co/THUDM/chatglm3-6b` 下载。`adapter_name_or_path` 则是我们在 huggingface 上的模型路径。`quantization_bit` 设置为 8 或 4 可以减少显存占用，但如果显存充足，这一设置也可以省略。

加载模型完成后，就可以开始交互了。例如：
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


### 声明

CoolShell LLM 模型旨在传承陈皓先生精神，勿将开源模型和代码及基于开源项目产生的衍生物用于任何可能给国家和社会带来危害的用途以及用于任何未经过安全评估和备案的服务。

尽管模型在训练的各个阶段都尽力确保数据的合规性和准确性，但由于模型受概率随机性因素影响，无法保证输出内容的准确。同时模型的输出容易被用户的输入误导。本项目不承担开源模型和代码导致的数据安全、舆情风险或发生任何模型被误导、滥用、传播、不当利用而产生的风险和责任。

