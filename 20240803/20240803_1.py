import os.path
#使用內建的 os.path
current_path = os.path.abspath (__name__) #path name
print(current_path)
current_dir = os.path.dirname (current_path)
print(current_dir)
data_path = os.path.join(current_dir,'data')
os.path.isdir(data_path)

if not os.path.isdir(data_path):
    os.mkdir(data_path)
    print("Process dir")
else:
    print("the data already exit:  " , data_path)


iot_pathWithName = os.path.join(data_path, 'iot.log')

print("logflie is local at ->   " ,iot_pathWithName)

if not os.path.isfile(iot_pathWithName):
    print("no log exit, will do the file creation the file")
    with  open(iot_pathWithName,mode='w',encoding='utf-8', newline='') as file:
        file.write('DateTime,H,T\n')
    # file.close()
else:
    print("file already exit ->>  ", iot_pathWithName )