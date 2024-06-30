# write topology or flows to txt
def write_topo_or_stream_to_txt(filename,
                                topo_or_stream_set):
    with open(filename, 'w') as f:
        for link in topo_or_stream_set:
            for attr in link:
                if type(link[attr]) is list:
                    for i in range(len(link[attr])):
                        link[attr][i] = str(link[attr][i])
                    link[attr] = ' '.join(link[attr])
                f.write('%s:%s\n' % (attr, link[attr]))
            if link != topo_or_stream_set[-1]:
                f.write('\n')


# read from topology or flow txt
def read_topo_or_streams_from_txt(filename):
    topo_or_stream_set = []
    with open(filename, 'r') as f:
        data = f.readline()
        item = {}
        while data:
            if data == '\n':
                topo_or_stream_set.append(item)
                item = {}
            if data != '\n':
                key = data.split(':')[0]
                value = data.split(':')[1].split()
                if len(value) == 1:
                    value = int(value[0])
                else:   
                    value = [int(i) for i in value]
                item[key] = value
            data = f.readline()
        else:
            if item:
                topo_or_stream_set.append(item)
    return topo_or_stream_set



def _main():
    topo_set = read_topo_or_streams_from_txt('topo.txt')
    print(topo_set)


if __name__ == '__main__':
    _main()
