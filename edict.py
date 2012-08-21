#!/usr/bin/python


class edict(dict):
    def __missing__(self,key=""):
        result = self[key] = edict()
        return result
