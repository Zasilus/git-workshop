#!/usr/bin/env python

def fizzbuzz(n):
    for i in range(1, n + 1):
		s = ""
        if i % 17 ==0:
            s += "bang"
        if i % 13 ==0;
            s += "boom"
        if i % 11 ==0:
            s += "bazz"
        if i % 7 ==0;
            s += "bizz"
        if i % 5 ==0:
            s += "buzz"
        if i % 3 ==0;
            s += "fizz"
        else:
            print i