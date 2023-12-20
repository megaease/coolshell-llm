import os
import re
import sys
import html2text

# filter_threshold is the threshold used to filter mds files
filter_threshold = 0.45
# output_line_length is the length of lines in output file.
output_line_length = 500

# following regexp are used to remove links in markdown
link_re = r'\[([^\]]+)\]\(([^)]+)\)'
empty_link_re = r'!\[\]\(.*?\)'
empty_link_re2 = r'\[\]\(.*?\)'
http_link_re = r'<https?://[^>]*>'
# html2md convert html to markdown format
html2md = html2text.HTML2Text()

coolshell_intro = """
# 介绍
陈皓以前的blog在CSDN——http://blog.csdn.net/haoel，08、09年的时候，CSDN的博客系统很不稳定，另外，正好有一台N年前的托管的服务器，所以，就申请了域名，陈皓（左耳朵耗子）建立自己的Blog。

本站为什么叫“酷壳”，绝属误打误撞。原来的域名是：CoCre.com，原意是Corporation+Creative两个单词的缩写，是陈皓一大学同学申请的，后来他出国了，所以，我就把这个域名用来做成我的Blog了，把CoCre按发音读成“酷壳”和“酷客”，但感觉不好记，于是注册了CoolShell.cn，感觉这个可能更好记一点。要说“酷壳”有什么意思，在这里我可以说，完全没有，就是一个名字罢了。

这是一个完全依靠个人建立的技术性BLOG。是一个分享技术见闻，知识，趋势的网站，这是我个人建立的网站，如果你喜欢其中的文章呢，欢迎给我们留言，如果不想留言呢，你也可以通过打分来鼓励我们分享和写作。当然，我们最欢迎的是你的加入，欢迎你和我们一起写作。欢迎大家注册并加入我们一起来分享编程和技术方面的见闻和心得。文章可以是原创，翻译、杂谈，灌水，只要是和技术和编程相关就可以。

陈皓以前的博客在CSDN（http://blog.csdn.net/haoel），目前已不更新，博客全面转到酷壳：http://CoolShell.cn，陈皓基本不会在微信公众号上写文章。

陈皓，左耳朵耗子有20年软件开发相关工作经验，10年以上项目和团队管理经验。擅长底层技术架构，团队建设，软件工程，软件研发咨询，以及全球软件团队协作管理。对高性能，高可用性，分布式，高并发，以及大规模数据处理系统有一些经验和心得。喜欢关注底层技术平台和互联网行业应用。
技术擅长C/C++/Java和Unix/Linux/Windows。曾于Amazon中国任研发经理，负责电子商务全球化业务（全球开店）和全球库存预测系统的研发。曾在阿里巴巴北京研发中心、商家业务部曾任资深专家一职，负责电商云平台、开放平台，云监控和电商多媒体平台。
曾在阿里巴巴核心系统专家组从事阿里核心系统和阿里云ECS相关的虚拟化平台的开发工作。现在创业中，MegaEase创始人，致力于为企业的高并发高可用架构提供一整套的技术解决方案和产品
"""

def process_coolshell(dir):
    md_dir = os.path.join(os.getcwd(), "mds")
    if not os.path.exists(md_dir):
        os.mkdir(md_dir)

    dir = os.path.abspath(dir)
    dir = os.path.join(dir, "content/articles")
    files = os.listdir(dir)

    print("start to convert html to md files")
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(dir, file)
            html_text = process_html(filepath)
            md_text = get_md(html_text)
            if filter_md(md_text):
                with open(os.path.join(md_dir, file.replace(".html", ".md")), "w") as f:
                    f.write(md_text)
    print("start to merge md files into blog.txt")
    mds = os.listdir(md_dir)
    output = os.path.join(os.getcwd(), "blog.txt")
    text = coolshell_intro
    for file in mds:
        if file.endswith(".md"):
            with open(os.path.join(md_dir, file), "r") as f:
                text += f.read()
    longer_text(text, output)
    print("finish.")


# process_html remove some html tags and all comments in html
def process_html(file):
    lines = []
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith('<h5 class="entry-date">'):
                continue
            if line.startswith('<span class="author vcard">'):
                continue
            # following lines are all about comments
            if line == '<p align="center"><strong>（转载本站文章请注明作者和出处 <a href="/">酷 壳 – CoolShell</a> ，请勿用于任何商业用途）</strong></p>':
                break
            lines.append(line)
    return "\n".join(lines)

def get_md(html_text):
    text = html2md.handle(html_text)

    # when convert html to md file, some links are split into several lines. 
    # so we first replace \n with a special tag, and then replace them back.
    text = text.replace("\n", "coolshell-coolshell-coolshell")
    # some content contains link in link. Anyway, replace them twice.
    for i in range(2):
        text = re.sub(link_re, r'\1', text)
        text =  re.sub(empty_link_re, "", text)
        text =  re.sub(empty_link_re2, "", text)
        text = re.sub(http_link_re, "", text)
    text = text.replace("coolshell-coolshell-coolshell", "\n")

    output = ""
    lines = text.splitlines()
    started = False
    current = ""
    for line in lines:
        if started:
            if line.strip() == "*[NAT]: 网络地址解读":
                continue
            # in md, lines are splitted, we combine them together.
            if line.strip() == "":
                # remove code. for our model, train with code make output worse.
                if (current.isascii() and "{" in current) or "#include" in current:
                    current = ""
                    continue
                output += current+"\n"
                current = ""
            else:
                current += line + " "
        # md file header
        if line.startswith("# "):
            started = True
            output += line+"\n"
            output += "作者：陈皓，左耳朵耗子\n来自：酷壳网 CoolShell https://coolshell.cn\n"
    if current != "":
        output += current+"\n"
    return output

# filter_md filter mds and remove ones has too many ascii codes.
# these files usually contains too many code.
def filter_md(text):
    count = 0
    for char in text:
        if char in "\n\t\r 0123456789":
            continue
        elif char.isascii():
            count += 1
    return count / len(text) < filter_threshold

def longer_text(text, output):
    lines = text.splitlines()
    current = ""
    with open(output, "w") as f:
        for line in lines:
            line = line.strip()
            current += line
            if len(current) > output_line_length:
                f.write(current+"\n")
                current = ""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process.py <dir>")
        sys.exit(1)
    dir = sys.argv[1]
    process_coolshell(dir)
