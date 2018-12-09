# coding: UTF-8
'''''''''''''''''''''''''''''''''''''''''''''''''''''
   file name: main.py
   create time: 2017年06月23日 星期五 16时41分54秒
   author: Jipeng Huang
   e-mail: huangjipengnju@gmail.com
   github: https://github.com/hjptriplebee
'''''''''''''''''''''''''''''''''''''''''''''''''''''
from config import *
import data
import model

def defineMode():
    mode = input("please input mode:")
    return mode

if __name__ == "__main__":
    mode = defineMode()
    trainData = data.POEMS(trainPoems)
    MCPangHu = model.MODEL(trainData)
    if mode == "train":
        MCPangHu.train()
    else:
        if mode == "test":
            poems = MCPangHu.test()
        else:
            characters = input("please input chinese character:")
            poems = MCPangHu.testHead(characters)