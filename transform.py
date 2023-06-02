import os

def loadDatadet(infile,k):
    f=open(infile,'r')
    sourceInLine=f.readlines()
    dataset=[]
    for line in sourceInLine:
        temp1=line.strip('\n')
        temp2=temp1.split( )
        dataset.append(temp2)
    for i in range(0,len(dataset)):
        for j in range(k):
            dataset[i].append(float(dataset[i][j]))
        del(dataset[i][0:k])
    f.close()
    return dataset

origin_dataset_path = '/home/liqianqi/BUFF/ENERGY/labels_1'
output_dir_path = '/home/liqianqi/BUFF/ENERGY/labels2'


k=11
if not os.path.exists(output_dir_path):
    os.mkdir(output_dir_path)
dataset = os.listdir(origin_dataset_path)
cnt = 0
for file in dataset:
    print(file)
    inputfile = origin_dataset_path + "/" +file
    input = open(inputfile,'r')

    if len(input.read()) == 0:
        outputfile = output_dir_path + "/" + file
        output = open(outputfile, 'w')
        output.close()

    else:
        one_file_data = loadDatadet(inputfile,k)
        outputfile = output_dir_path + "/" + file
        output = open(outputfile, 'w')

        for line in one_file_data:
            names = line[0]
            tempx = line[1:11:2]
            tempy = line[2:11:2]
            xmax = max(tempx)
            ymax = max(tempy)
            xmin = min(tempx)
            ymin = min(tempy)
            xcenter = (xmax+xmin)/2
            ycenter = (ymax+ymin)/2
            w = xmax - xmin
            h = ymax - ymin
            output.write(str(round(names,1)) + " " + str(round(xcenter,6)) + " " + str(round(ycenter,6)) + " " + str(round(w,6)) + " " + str(round(h,6)))
            for i in range(1,11):
                output.write(" " + str(line[i]))
            # output.write(" " + "-1" + " " + "-1" )
            output.write("\n")
        output.close()
    # cnt = cnt + 1
    # print(cnt)