
from time import localtime,time

def main():

    curentTime=time()
    loc=localtime(curentTime)
    print(loc)
    # first find date if i'ts not first start
    # we don't need it
    # then if its' not first add line with date and start time
    myfile=openFile("worktime"+str(loc.tm_year)+str(loc.tm_mon)+'.csv','a')
    myfile.write('start:;'+str(loc.tm_year)+';'+str(loc.tm_mon).format('%02d')+';'+str(loc.tm_mday)+';'+str(loc.tm_hour)+':'+str(loc.tm_min)+':'+str(loc.tm_sec)+';'+str(loc.tm_hour*3600+loc.tm_min*60+loc.tm_sec)+';')
    myfile.close()


def openFile(name,atributes):
    try:
        myfile = open(name, atributes)
    except FileNotFoundError:
        print('filenotFound, create new one')
        myfile = open(name, 'w')
        myfile.close()

    return myfile

if __name__ == '__main__':
    main()
