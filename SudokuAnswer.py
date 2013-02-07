__author__ = 'gyyan'
import types
import copy

def dealSingleUnit( dataList, val):
    doSomeThing = False
    judgeOneUnit = False
    if type(dataList) == types.ListType  and type(val) == types.IntType:
        if val in dataList:
            doSomeThing = True
            dataList.remove(val)
            if len(dataList) == 1:
                dataList = dataList[0]
                judgeOneUnit = True

    return (doSomeThing, judgeOneUnit, dataList)

def PrintFindRes(data, i, j):
    print 'judge %d %d : %d'%(i, j, data[i][j])
    res = judgeRight(data)
    if res == False:
        print "ERROR"
        #exit(0)

def printData(data):
    for i in range(1, 10):
        for j in range(1, 10):
            print ' ',data[i][j],
            if j%3 == 0:
                print ' ',
        print '\n',
        if i%3 == 0:
            print '\n'

def judgeRight(data):
    for i in range(1, 10):
        for j in range(1, 10):
            if type(data[i][j]) == types.IntType:
                #judge row
                for jj in range(1,10):
                    if jj == j:
                        continue
                    if data[i][j] == data[i][jj]:
                        return False
                #judge col
                for ii in range(1,10):
                    if i == ii:
                        continue
                    if data[i][j] == data[ii][j]:
                        return False
                #judge same Unit
                iStart = (i-1)/3*3 +1
                jStart = (j-1)/3*3 +1
                for iStarti in range(iStart, iStart+ 3):
                    for jStartj in range(jStart, jStart + 3):
                        if iStarti == i and jStartj == j:
                            continue
                        if data[i][j] == data[iStarti][jStartj]:
                            return False

    return True


def FindSuduku(data):
    doSomeThingRes = False
    for i in range(1, 10):
        for j in range(1, 10):
            if type(data[i][j]) == types.ListType:
                judgeOneUnit = False
                #deal row same
                for jj in range(1, 10):
                    if jj == j:
                        continue
                    doSomeThing, judgeOneUnit, data[i][j] = dealSingleUnit(data[i][j], data[i][jj])
                    if doSomeThing:
                        doSomeThingRes = True
                    if judgeOneUnit:
                        PrintFindRes(data, i, j)
                        return (doSomeThingRes, judgeOneUnit)
                #deal col same
                for ii in range(1, 10):
                    if ii == i:
                        continue
                    doSomeThing, judgeOneUnit, data[i][j] = dealSingleUnit(data[i][j], data[ii][j])
                    if doSomeThing:
                        doSomeThingRes = True
                    if judgeOneUnit:
                        PrintFindRes(data, i, j)
                        return (doSomeThingRes, judgeOneUnit)
                #deal same unit
                iStart = ((i -1)/3)*3 +1
                jStart = ((j-1)/3)*3 +1
                for iStarti in range(iStart, iStart+ 3):
                    for jStartj in range(jStart, jStart + 3):
                        if i == iStarti and j == jStartj:
                            continue
                        doSomeThing, judgeOneUnit, data[i][j] = dealSingleUnit(data[i][j], data[iStarti][jStartj])
                        if doSomeThing:
                            doSomeThingRes = True
                        if judgeOneUnit:
                            PrintFindRes(data, i, j)
                            return (doSomeThingRes, judgeOneUnit)
    return (doSomeThingRes, False)

def judgeSomeUnit(data):
    for i in range(1,4):
        for j in range(1,4):
            #Judge On Unit 3x3
            iStart = (i-1)*3+1
            jStart = (j-1)*3+1
            for iStarti in range(iStart, iStart+3):
                for jStartj in range(jStart, jStart+3):
                    if type(data[iStarti][jStartj]) == types.ListType:
                        tmplist = data[iStarti][jStartj][:]
                        for listVali in range(iStart, iStart+3):
                            for listValj in range(jStart, jStart+3):
                                if listVali == iStarti and listValj == jStartj:
                                    continue
                                if type(data[listVali][listValj]) == types.ListType:
                                    for val in data[listVali][listValj]:
                                        if val in tmplist:
                                            tmplist.remove(val)
                        if len(tmplist) == 1:
                            data[iStarti][jStartj] = tmplist[0]
                            PrintFindRes(data, iStarti, jStartj)
                            return True
    return False

def relatedrowcolJudge(data):
    doSomeThingRes = False
    for i in range(1, 4):
        for j in range(1, 4):
            #Judge On Unit 3x3
            iStart = (i-1)*3+1
            jStart = (j-1)*3+1
            for iStarti in range(iStart, iStart+3):
                for jStartj in range(jStart, jStart+3):
                    if type(data[iStarti][jStartj]) == types.ListType:
                        for val in data[iStarti][jStartj]:
                            #judge row
                            rowres = True
                            for iStartii in range(iStart, iStart + 3):
                                for jStartjj in range(jStart, jStart +3):
                                    if iStartii == iStarti:
                                        continue
                                    if type(data[iStartii][jStartjj]) == types.ListType:
                                        if val in data[iStartii][jStartjj]:
                                            rowres = False
                                            break
                                if rowres == False:
                                    break
                            if rowres:
                                tmprange = range(1, 10)
                                tmprange = list(set(tmprange) - set(range(jStart, jStart +3)))
                                for j1 in tmprange:
                                    (doSomeThing, judgeOneUnit, data[iStarti][j1]) = dealSingleUnit( data[iStarti][j1], val)
                                    if doSomeThing:
                                        doSomeThingRes = True
                                    if judgeOneUnit:
                                        PrintFindRes(data, iStarti, j1)
                                        return (doSomeThingRes, judgeOneUnit)

                            #judge col
                            colres = True
                            for iStartii in range(iStart, iStart + 3):
                                for jStartjj in range(jStart, jStart +3):
                                    if jStartjj == jStartj:
                                        continue
                                    if type(data[iStartii][jStartjj]) == types.ListType:
                                        if val in data[iStartii][jStartjj]:
                                            colres = False
                                            break
                                if colres == False:
                                    break
                            if colres:
                                tmprange = range(1, 10)
                                tmprange = list(set(tmprange) - set(range(iStart, iStart +3)))
                                for i1 in tmprange:
                                    (doSomeThing, judgeOneUnit, data[i1][jStartj]) = dealSingleUnit( data[i1][jStartj], val)
                                    if doSomeThing:
                                        doSomeThingRes = True
                                    if judgeOneUnit:
                                        PrintFindRes(data, i1, jStartj)
                                        return (doSomeThingRes, judgeOneUnit)

    return (doSomeThingRes, False)

def FindSuduResStep1(data):
    findCount = 0
    for findCount in range(1, 1000):
        doSomeThing, judgeSomeThing = FindSuduku(data)
        if doSomeThing == False:
            unitJudgeRes = judgeSomeUnit(data)
            if unitJudgeRes == False:
                d1,j1 = relatedrowcolJudge(data)
                if d1 == False:
                    break
    return findCount

def SuduIsCompeleted(data):
    for i in range(1,10):
        for j in range(1, 10):
            if type(data[i][j]) == types.ListType:
                return False
    return True

def GetNeedGuess(data):
    for i in range(1, 10):
        for j in range(1, 10):
            if type(data[i][j]) == types.ListType:
                return [i, j, data[i][j]]
    print "Error: Can't Guess"

if __name__ == '__main__':
    problemfile = open("1.txt")
    filecontent = problemfile.read()
    print"filecontent: \n", filecontent
    problemfile.close()
    print "Read Data Over"

    filecontent = filecontent.split()

    print "Init suduku data Start"
    sampledata = range(1,10)
    sudokudata = {}
    for i in range(1, 10):
        sudokudata[i] = {}
        for j in range(1, 10):
            sudokudata[i][j] = int(filecontent[(i -1)*9 + (j-1)])
            print " %d"%sudokudata[i][j],
            if sudokudata[i][j] == 0:
                sudokudata[i][j] = sampledata[:]
        print "\n",

    print "Init suduku data Over"

    print "Start find answer"
    findCount = 0
    guessedTestList = []
    findCount += FindSuduResStep1(sudokudata)

    if SuduIsCompeleted(sudokudata) == False:
        for i in range(1,1000):
            copyedSudokudata = copy.deepcopy(sudokudata)
            if len(guessedTestList) > 0:
                for testListVal in guessedTestList:
                    copyedSudokudata[testListVal[0]][testListVal[1]] = testListVal[2]
            findCount += FindSuduResStep1(copyedSudokudata)
            if judgeRight(copyedSudokudata):
                if SuduIsCompeleted(copyedSudokudata):
                    print "** GetAnswer **"
                    sudokudata = copyedSudokudata
                    break
                else:
                    guesslist = GetNeedGuess(copyedSudokudata)
                    guessedTestList.append([guesslist[0], guesslist[1], guesslist[2][0], 0, guesslist[2][:]])
            else:

                upVal = guessedTestList[-1]
                index = upVal[3]
                index+=1
                while index >= len(upVal[4]) and len(guessedTestList) >= 1:
                    guessedTestList.pop()
                    upVal = guessedTestList[-1]
                    index = upVal[3]
                    index += 1
                upVal[3] = index
                upVal[2] = upVal[4][index]


    print "Find Answer Use %d Count" %findCount
    for i in range(1, 10):
        for j in range(1, 10):
            print ' ',sudokudata[i][j],
            if j%3 == 0:
                print ' ',
        print '\n',
        if i%3 == 0:
            print '\n'





