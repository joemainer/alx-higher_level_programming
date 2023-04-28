#!/usr/binpython3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_na,e = "John"
try:
	lc.lastname ="Snow"
exept Exeption as e:
