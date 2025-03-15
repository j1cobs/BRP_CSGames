import yaml
import json


serverArr = []

apps =  {
 'Terraform': 'TFM',
 'Ad Manager Plus': 'ADP',
 'Jira': 'JIR',
 'Confluence': 'CFL',
 'Saleforce': 'SFC',
 'Nagios': 'NAG',
 'IT Service Management': 'ITS',
 'Keeper': 'KEE',
 'Kofax': 'KFX',
 'Mantis BT': 'MTS'
}

countryList = ["CA", "US", "FR", "SG", "JP", "BR", "MX"]

envs = ["D", "P", "T", "S"]

roles = {
 'Back End': 'BE',
 'Front End': 'FE',
 'Database': 'DB',
 'Load balancer': 'LB',
 'Monitor': 'MO'
}


def readServerFile():
    for i in range (1, 1307):
        fileName = str(i)
        while(len(fileName) < 8):
            fileName = '0' + fileName
        fileName += '.yml'
        fileName = "../data/servers/" + fileName
        # file = open("../data/fileName"); 
        with open(fileName, 'r') as f:
            data = yaml.full_load(f)
        serverArr.append(data)
        # outputFile.write(serverName + '\n')

    # outputFile.close()


def writeServerFile():
    outputFile = open("output.txt", "w")
    for server in serverArr:
        outputFile.write(server.get('name') + '\n')
    outputFile.close()


def getCorrectName(server):
    serverName = server.get('name')

    # countryCode = serverName[0:2]
    # applicationCode = serverName[2:5]
    # roleCode = serverName[5:7]

    envCode = serverName[7:8]
    numberCode = serverName[8:13]

    correctCountryCode = server.get('tags').get('country')
    correctApplicationCode = apps[server.get('tags').get('app')]
    correctRoleCode = roles[server.get('tags').get('role')]

    correctServerName = correctCountryCode + correctApplicationCode + correctRoleCode + envCode + numberCode

    return correctServerName



def analyzeServerName():
    fileContent = "{" + '\n'
    for server in serverArr:
        serverName = server.get('name')
        correctName = getCorrectName(server)
        if (serverName != correctName):
            output = '"' + serverName + '"' + " : " + '"' + correctName +'"' + "," + '\n'
            fileContent += output
    fileContent += "}"

    f = open("../data_output/wrong_name.json", "w")
    f.write(fileContent)
    f.close()

        
def main():
    readServerFile()
    analyzeServerName()

main()

