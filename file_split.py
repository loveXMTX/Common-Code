import os
import time
import sys

#  This function is from CSDN,I encapsulated it a little
#  Upload is for easy use in the future
# Because I don't remember where I saw it, I don't add a link.
# If there is any infringement, I will delete it immediately.

#  des_filename : 路径名
#  srcName        文件路径包括扩展名
#  sub            第几个切割文件
#  head           csv的表头
#  lines          写入的内容
def mkSubFile(lines, head, srcName, sub):
    [des_filename, extname] = os.path.splitext(srcName)
    filename = des_filename + '_' + str(sub) + extname
    print('make file: %s' % filename)
    fout = open(filename, 'w')
    try:
        fout.writelines([head])
        fout.writelines(lines)
        return sub + 1
    finally:
        fout.close()

#  count：每次要切割的行数
#  filename：文件名路径

def splitByLineCount(filename, count):
    fin = open(filename, 'r')
    try:
        head = fin.readline()
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == count:
                sub = mkSubFile(buf, head, filename, sub)
                buf = []
        if len(buf) != 0:
            sub = mkSubFile(buf, head, filename, sub)
    finally:
        fin.close()


if __name__ == '__main__':
    csv_dir=sys.argv[1]
    file_split_per_count=int(sys.argv[2])
    begin = time.time()
    splitByLineCount(csv_dir,file_split_per_count)
    end = time.time()
    print('time is %d seconds ' % (end - begin))