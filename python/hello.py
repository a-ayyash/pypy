#!/usr/local/bin/python

print("hello");

def funf(*modules):
    for module in modules:
        print module

funf('generator.supports')
