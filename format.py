def read_csv(filename):
    with open(filename) as f:
        l = f.readlines()
    l = [i.split(",") for i in l]
    return l

def consistent(arr):
    n = len(arr)
    m = len(arr[0])
    for i,val in enumerate(arr):
        if not len(val) == m:
            print("Not consistent at row {} with value {} instead of {}".format(i+1,len(val),m))
            exit(1)

    else:
        print("Consistent with {}X{}".format(n,m));

def main():
    for i in range(1):
        cfl = read_csv('./fit_data/cfl_4km.csv')
        cfm = read_csv('./fit_data/cfm_4km.csv')
        cfh = read_csv('./fit_data/cfh_4km.csv')
        swflx = read_csv('./fit_data/swflx_4km.csv')
        temp = read_csv('./fit_data/temp_4km.csv')
        rows = len(swflx)
        consistent(cfl)
        consistent(cfm)
        consistent(cfh)
        consistent(swflx)
        consistent(temp)
        for panel in range(1,170):
            with open("./panels/panel%d.csv"%(panel), "w") as f:
                for row in range(rows):
                    new_row = [
                            cfl[row][0], 
                            cfl[row][panel], 
                            cfm[row][panel], 
                            cfh[row][panel], 
                            swflx[row][panel],
                            temp[row][panel]
                            ]
                    f.write(','.join(new_row))
                    f.write('\n')
            print("Done: panel%d.csv"%(panel))




if __name__ == "__main__":
    main()
