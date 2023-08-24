def read_csv(filename):
    with open(filename) as f:
        l = f.readlines()
    l = [i.split(",") for i in l]
    return l


def main():
    for i in range(1):
        cfl = read_csv('./processed_data/modified_cfl_4km.csv')
        cfm = read_csv('./processed_data/modified_cfm_4km.csv')
        cfh = read_csv('./processed_data/modified_cfh.csv')
        swflx = read_csv('./processed_data/modified_swflx.csv')
        temp = read_csv('./processed_data/modified_temp_4km.csv')
        print(
                len(cfl),
                len(cfm),
                len(cfh),
                len(swflx),
                len(temp)
                )

if __name__ == "__main__":
    main()
