from format import read_csv
from os import system
from os.path import isfile

def clean(filename):
    table = read_csv("dataset/"+filename)
    prev = table[1][0]
    temp = []
    final = [] 
    st = set()
    for row in table[1:]:
        temp.append(row)
        if row[0] == prev:
            continue;
        else:
            st.add(prev)
            ins = [prev]
            for cell in range(2,171):
                s = 0;
                for i in range(len(temp)):
                    s += float(temp[i][cell])
                s /= len(temp)
                ins.append(s)
            final.append(ins)
            prev = row[0]
            temp.clear()
    print(len(final))
    table[0].remove('timerequests')
    with open("fit_data/"+filename, "w") as f:
        f.write(",".join(table[0]))
        for i in final:
            f.write(",".join([str(elem) for elem in i]))
            f.write('\n')

def download():
    file = "https://rdm.inesctec.pt/dataset/d5700c25-c3f2-4f51-922a-87b450df1ebd/resource/b29a9f98-acd5-4f43-afb6-8ce4e314e9a1/download/nwpdatasets.zip"
    system("curl {} > dataset.zip".format(file))
    system("unzip dataset.zip")
    system("mv NWP_datasets/* dataset/")
    system("rmdir NWP_datasets")

def main():
    if not isfile('dataset.zip'):
        download()
    files = [
            "cfh_4km.csv",
            "cfl_4km.csv",
            "cfm_4km.csv",
            "cft_4km.csv",
            "swflx_4km.csv",
            "temp_4km.csv",
            ]
    for i in files:
        clean(i)
        print("Done: {}".format(i))



if __name__ == "__main__":
    main()
