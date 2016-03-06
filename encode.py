#! /usr/bin/python

import json
import sys, os

class test(object):
	"testing class"
	def __init__(self, name = "", age = 0):
		pass
		self.name = "MyName"
		self.age = 10
	def display(self):
		print "I'm test class!"
	def __repr__(self):
		pass
		#return "name: %s, age: %d" %(self.name, self.age)

def object2dict(obj):
	"object (class) to dictionary"
	d = {}
	d["__class__"] = obj.__class__.__name__
	d["__module__"] = obj.__module__
	d.update(obj.__dict__)
	return d

def dict2object(d):
	"dictionary to object (class)"
	if "__class__" in d:
		class_name = d.pop("__class__")
		module_name = d.pop("__module__")
		module = __import__(module_name)
		class_ = getattr(module, class_name)
		args = dict( (key.encode("ascii"), value) for key, value in d.items() )
		print "class params: ", args
		inst = class_(**args)
	else:
		inst = d
	return inst


if __name__ == "__main__":
	print "json test ..."

	obj = test("thompson", 23)

	dic = object2dict(obj)
	dic_encoded = json.dumps(dic)
	with open("encoded.txt", "w") as df:
		df.write(dic_encoded)

	obj_decoded = dict2object(dic)


