#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for jarvis in dir(hidden_4):
        if (jarvis[0] != "_"):
            print(jarvis)
