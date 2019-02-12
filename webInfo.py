from robot_txt_finder import get_robot_txt
import os

def nm(ip_a):
    cm = 'nmap -v -O -A ' + ip_a

    pr = os.popen(cm)

    re = str(pr.read())

    return re


def ip_address(url):
    command = "host " + url

    process = os.popen(command)

    result = str(process.read())

    marker = result.find('has address') + 12
    return result[marker:].splitlines()[0]


#************ for whoislook ************#


def whoisLook(url):
    cm = 'whois ' + url

    pros =  os.popen(cm)

    result  = str(pros.read())

    return result



#************ for figlet ************#

try:
    def font():
        command1 = 'figlet -f big ' + 'webInfo'
        command2 = 'figlet -f mini -c ' + 'Arthur : Rajdip Mondal'
        command3 = "echo 'contact me : rajdipm65@gmail.com'"

        proc1 = os.popen(command1)

        
        proc2 = os.popen(command2)
        proc3 = os.popen(command3)
        result1 = str(proc1.read())
        result2 = str(proc2.read())
        result3 = str(proc3.read())

        print(result1)
        print(result2)
        print(result3)

except TypeError as tE:
    print("type wrong input")

except Exception:
    command = 'sudo apt install figlet -y'
    ex = os.popen(command)



font()
user_domin = str(input("enter terget domin name : "))
print("wait please ")
print(ip_address(user_domin))
ip = ip_address(user_domin)





print("Nmap Scaning Start ")

nmap_var = nm(ip)
print("Nmap Scaning Complete")
print("Now Starting Whois")
whoIS =  whoisLook(user_domin)
print("\t Now Start Chaking Robots.txt ")
fullDomin = 'http://' + user_domin
try:
    robot = get_robot_txt(fullDomin)
except ValueError as vE:
    print("Don't Have Robot.txt file in this site" ,vE)
except urllib.error.HTTPError as lE:
    print("Don't Have Robot.txt file in this site",lE)
except Exception:
    print("robot txt finding faild ")





try:
    nmap_var_full = nmap_var + whoIS + robot

except NameError as nE:
    nmap_var_full = nmap_var + whoIS
print("Now all done Save Result in txt File \n")
inputFilePath = input("enter the path for save this result file : ")
inputFileName = input("\nenter file name don't use any extansion : ")
inputFile = inputFilePath + inputFileName + '.txt'

file = open(inputFile,'w')
file.write(nmap_var_full)

print(nmap_var_full)
