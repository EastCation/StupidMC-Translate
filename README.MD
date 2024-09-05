# StupidMC Translate——沙雕翻译包源码库

## PRISM Codeopen Project/已列入棱镜开源计划

>[英文文档](README_EN.MD)还在准备中，欢迎帮助辉夜翻译！  
>[English docs](README_EN.MD) stills preparing, welcome to help Starmoe to translate it！

## 介绍

这是辉夜星瞳与棱镜开发组的作品——沙雕翻译包。本翻译包具有跟APT一样的强大力量。

## 文件结构

当前版本的沙雕翻译包文件结构如下所示。（*表示下载后可自行删除，不影响使用）

```Python

 <ROOT>
    [assets]
    <pack.mcmeta>#资源包元文件，删除将导致资源包不可用
        [bedrockify]#兼容Bedrockify的模块
            [lang]
                <zh_cn.json>
        [minecraft]#原版兼容Minecraft的模块
            [lang]#语言文件
                *<en_us.json>#英文原版语言文件（可能过时）
                <zh_cn.json>#沙雕翻译包核心——中文语言文件
                *<zh_cn-233.json>#旧版社区语言文件，未翻译完
            [texts]#通用文本文件（例如终末之诗和演职员表）
                <credits.json>#现在的演职员表
                <credits.txt>#为向下兼容打造的旧版演职员表（停止更新）
                <end.txt>#终末之诗原文以及翻译
                <end.txt.bak>#以上文件的副本
                <postcredits.txt>#终末之诗及演职员表后的那段寄语
                <splashes.js>#向下兼容的闪烁标语（停止更新）
                <splashes.txt>#主界面闪烁的黄色的沙雕文本（闪烁标语）


```

## 用法

### Modrinth版本下载（推荐）

如果您的启动器自带从Modrinth检索资源包的功能，您可以直接搜索"Stupid MC"，之后按照启动器的说明安装即可。

如果您的启动器不带有从Modrinth检索资源包的功能，您可以通过[此链接](https://modrinth.com/resourcepack/stupid-mc-translate-chn)进行下载，Modrinth的zip无需解压，直接放在资源包文件夹即可使用。

### git版本下载

在[这里下载发行版](https://github.com/EastCation/StupidMC-Translate/releases)，拿到压缩包后将里面的<StupidMC-Translate-版本>放到你的版本的[resourcespacks]文件夹下，之后在Minecraft的资源包选取界面应该就可以看到，加载在最上面即可（本包无纹理改动功能，请放心使用）

## 与其他资源包的反应

本资源包可与梗体中文资源包合并使用；但在使用前请确保您的梗体中文资源包启用了*兼容模式*且此资源包在最顶端，否则您将只能看到梗体中文的翻译。

本资源包建议配合沙雕附加包使用，否则可能会少了很多乐趣。

## 如何贡献

您需要Fork或者Git这个仓库，之后在本地创作您的杰作，如果您认为以及创作完毕，提交PR即可

如果PR出现了冲突，我们首先会遵循“先来后到”原则，如果后者有比前者更为优质的翻译，我们将会考虑后者而不是前者。

如果您对此资源包有任何疑问，欢迎开issue与我们一起讨论。

如果是涉及到个人隐私，您也可以发送邮件到[starmoe@starmoe.com.mp](mailto:starmoe@starmoe.com.mp)，我们会尽全力解决。

## 开源许可

本翻译包使用[GNU GPLv3](LICENSE)许可条款进行许可.

