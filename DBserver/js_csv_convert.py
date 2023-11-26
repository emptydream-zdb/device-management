__author__ = "Emptydream"

import sys as s
import json as js
import csv


def _dealList(jsDict, baseKey, keyVal):
    for x in range(len(keyVal)):
        _dealDict(jsDict, baseKey + str(x+1)+"_", keyVal[x])
    return


def _dealDict(jsDict, baseKey, keyVal):
    for key in keyVal.keys():
        if type(keyVal[key]) is list:
            _dealList(jsDict, baseKey + key, keyVal[key])
        elif type(keyVal[key]) is dict:
            _dealDict(jsDict, baseKey + key + "_", keyVal[key])
        else:
            jsDict[baseKey + key] = keyVal[key]
    return

def _dealunder(jsDict: dict) -> dict:
    keyList = list(jsDict.keys())
    velList = list(jsDict.values())
    lenth = len(keyList)
    begin = 0
    while begin < lenth:
        index = keyList[begin].find("_")
        if index != -1:
            baseKey = keyList[begin][0:index]
            end = begin + 1
            for x in keyList[begin + 1:]:
                index_end = keyList[end].find("_")
                if x[0:index_end] != baseKey:
                    break
                end += 1
            if end == begin+1:
                begin += 1
                continue
            velList[begin] = {keyList[i][index + 1:]: velList[i] for i in range(begin, end)}
            keyList[begin] = baseKey
            for i in range(begin + 1, end):
                keyList.pop(begin + 1)
                velList.pop(begin + 1)
            velList[begin] = _dealunder(velList[begin])

        begin += 1
        lenth = len(keyList)
    return {keyList[i]: velList[i] for i in range(len(keyList))}

def _dealnum(jsDict) -> dict:
    keyList = list(jsDict.keys())
    velList = list(jsDict.values())
    for x in velList:
        if type(x) is dict:
            x = _dealnum(x)
    lenth = len(keyList)
    begin = 0
    while begin < lenth:
        if keyList[begin][-1].isdigit():
            baseKey = keyList[begin][:-1]
            end = begin + 1
            for x in keyList[begin + 1:]:
                if x[:-1] != baseKey or not x[-1].isdigit():
                    break
                end += 1
            if end == begin + 1:
                begin += 1
                continue
            velList[begin] = [x for x in velList[begin:end]]
            keyList[begin] = baseKey
            for i in range(begin + 1, end):
                keyList.pop(begin + 1)
                velList.pop(begin + 1)
        begin += 1
        lenth = len(keyList)
    return {keyList[i]: velList[i] for i in range(len(keyList))}

def _expand(jsDict: dict) -> dict:
    jsDict = _dealunder(jsDict)
    jsDict = _dealnum(jsDict)
    return jsDict

def js_to_csv(file, foutName=None,mode='w'):
    """ convert a json file to csv

    :param file: str or list of the converted json obj
    :      foutName: if it is not None, will write in the fileName, else will return list
    """
    if type(file) == str:
        with open(file, 'r') as fin:
            jsObject = js.load(fin)
    else:
        jsObject = file
    if isinstance(jsObject, dict):
        jsObject = [jsObject]
    
    jsonList = [{} for x in range(len(jsObject))]
    for x in range(len(jsObject)):
        _dealDict(jsonList[x], "", jsObject[x])
    csvTitle = []
    for x in jsonList:
        i = 0
        for key in x.keys():
            if key not in csvTitle:
                csvTitle.insert(i,key)
            i += 1 
    if foutName != None:
        with open(foutName,mode) as fout:
            DictWrite = csv.DictWriter(fout, csvTitle, restval='')
            if mode == 'w':
                DictWrite.writeheader()
            DictWrite.writerows(jsonList)
        return 
    # TODO: return a list


def csv_to_js(filename, foutName=None):
    """convert a csv file to json

    :param filename: str, the path of converted file
    :      foutName: if it is not None, will write in the fileName, else will return list
    """
    with open(filename, 'r', newline='') as fin:
        csvReader = csv.DictReader(fin)
        dataList = []
        for x in csvReader:  # x is dict
            x = _expand(x)
            dataList.append(x)
        if len(dataList) == 1:
            dataList = dataList[0]
    if foutName != None:
        with open(foutName,'a') as fout:
            js.dump(dataList, fout)
        return
    return dataList


def convert_to_file(filename, direct):
    if direct == "-b":
        csv_to_js(filename,filename.rstrip(".csv") + ".json")
        return
    js_to_csv(filename,filename.rstrip(".json") + ".csv")
    return


if __name__ == "__main__":
    if len(s.argv) < 3:
        print("please input the correct parameters!")
        s.exit()
    convert_to_file(s.argv[2], s.argv[1])
