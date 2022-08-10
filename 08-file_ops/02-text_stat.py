#!/usr/bin/python3
import os

with open("test.txt", mode="w", encoding="utf-8") as text:
    text.write("Lorem ipsum dolor sit amet\nQuid secondom addicta\nest ese percipi\ngo lolo lo gollolo buga oh\n")
with open("test.txt", encoding="utf-8") as text:
    lineCount = 1
    while True:
        total = 0
        line = text.readline()
        if not line:
            break
        words = line.split(" ")
        for i in range(0, len(words)):
            total += len(words[i])
        avg = total / len(words)
        print(f"line {lineCount} : {line}contains {len(words)} words and an average of {avg:.1f} characters per word")
        lineCount += 1
        print()
