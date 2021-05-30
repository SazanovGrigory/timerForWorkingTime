from time import localtime,time
import subprocess

def getLineCountOfFile(name):
    lines=0
    myfile=openFile(name,'r')
    for line in myfile: 
        lines+=1
    myfile.close()
    return lines


def main():
    curentTime=time()
    loc=localtime(curentTime)
    print(loc)
    # first find date if i'ts not first start
    # we don't need it
    # then if its' not first add line with date and start time
    #get lines count
    name="worktime"+str(loc.tm_year)+str(loc.tm_mon)+".csv"
    lines=str(getLineCountOfFile(name))
    comment=input("Комментарий?")
    myfile=openFile(name,'a')
    myfile.write(' ;finish:;'+str(loc.tm_year)+';'+str(loc.tm_mon).format('%02d')+';'+str(loc.tm_mday)+';'+str(loc.tm_hour)+':'+str(loc.tm_min)+':'+str(loc.tm_sec)+';'+str(loc.tm_hour*3600+loc.tm_min*60+loc.tm_sec)+';отработанно;секунд;=M'+lines+'-F'+lines+';минут;=P'+lines+'/60;часов;=R'+lines+'/60;'+comment+';\n')
    myfile.close()
    subprocess.run('shutdown -s')


def openFile(name,atributes):
    try:
        myfile = open(name, atributes)
    except FileNotFoundError:
        print('filenotFound, create new one')
        myfile = open(name, 'w')
        myfile.close()

    return myfile


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
