虚拟的 Python 环境（简称 venv） 是一个能帮助你在本地目录安装不同版本的 Python 模块的 Python 环境，你可以不再需要在你系统中安装所有东西就能开发并测试你的代码。


virtualenv 的安装
创建虚拟环境
激活虚拟环境
使用多个虚拟环境
关闭虚拟环境

首先安装 pip3，打开 xfce 终端输入下面的命令：
```
$ sudo apt-get update
$ sudo apt-get install python3-pip

$ sudo pip3 install virtualenv
```
我们会创建一个叫做 virtual 的目录，在里面我们会有两个不同的虚拟环境


```
$ cd /home/shiyanlou
$ mkdir virtual
```
下面的命令创建一个叫做 virt1 的环境。

```
$ cd virtual
$ virtualenv virt1
```

New python executable in /home/shiyanlou/virtual/virt1/bin/python
Installing setuptools, pip, wheel...
done.

现在我们激活这个 virt1 环境。

```
$ source virt1/bin/activate
(virt1)shiyanlou：~/$
```
提示符的第一部分是当前虚拟环境的名字，当你有多个环境的时候它会帮助你识别你在哪个环境里面。
现在我们将安装 redis 这个 Python 模块。


```
(virt1) shiyanlou:virtual/ $ sudo pip3 install redis  
```
Installing collected packages: redis
Successfully installed redis-3.3.11

使用 deactivate 命令关闭虚拟环境。
```
(virt1)$ deactivate
$
```
现在我们将创建另一个虚拟环境 virt2，我们会在里面同样安装 redis 模块，但版本是 2.8 的旧版本。


```
$ virtualenv virt2
$ source virt2/bin/activate
(virt2)$ sudo pip3 install redis==2.8
```
Successfully built redis
Successfully uninstalled redis-3.3.11
Successfully installed redis-2.8.0