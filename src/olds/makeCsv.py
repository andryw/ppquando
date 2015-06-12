from sys import argv	

programacao = open("../programacao.txt","r")


csv = ""
for line in programacao:
    if "junho" in line or "julho" in line:
        if (len(csv) > 0):
            print csv[:-1]
        partesData = line.replace("\n","").split(" ")
        data = partesData[0] + "/" + ("06" if partesData[1] == "junho" else "07") + "/15"
        csv = data + ","
    else:
        csv += line.replace("\n","") + ","
