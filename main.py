import pandas
if __name__ == '__main__':
    data = open('addr_customers.txt', 'r', encoding='utf8')
    addr_list = [(line.strip()).split() for line in data]
    zipList = [(v, l[len(l) - 1]) for v, l in enumerate(addr_list)]
    zips = [l[len(l) - 1] for l in addr_list]
    zips = set(zips)

# todo : all list intersection items must be separated
    max_ids = []
    for i in range(1, len(zipList)):
        z1 = zipList[i-1]
        z2 = zipList[i]
        if z1[1] != z2[1]:
            # print(z1[1], z2[1])
            max_id = z2[0]
        max_ids.append(max_id)

    ids = sorted(set(max_ids))
    list_of_sets = []
    counted_list = []
    for i in range(1, len(ids)):
        start = ids[i - 1]
        end = ids[i]
        sublist_1 = addr_list[start:end]
        flat_list = [item for sublist in sublist_1 for item in sublist]
        flat_set = set(flat_list)
        list_of_sets.append(flat_set)
        list_t = []
        for item in flat_set:
            if flat_list.count(item) >= 3 and item != zipList[start][1] and len(item) > 2:
                counted_list.append((zipList[start][1], item, flat_list.count(item)))
    add_df = pandas.DataFrame(counted_list, columns=['zip', 'item', 'count_occurrence'])

    p_i_l = []
    for z in zips:
        t_1 = add_df[add_df['zip'] != str(z)]
        t_2 = add_df[add_df['zip'] == str(z)]
        public_items_list = t_1['item'].to_list()
        private_items_list = t_2['item'].to_list()
        p = [value for value in private_items_list if value in public_items_list]
        p_i_l.append(p)
        # print(len(p_i_l))
    print(len(p_i_l))
    print(p_i_l)

    add_df.to_excel('counted_columns.xlsx')
