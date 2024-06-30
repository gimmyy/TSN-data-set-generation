from ast import IsNot
from random import randint, choice
import matplotlib.pyplot as plt
import networkx as nx
from txt_engine import write_topo_or_stream_to_txt
import copy
import random
import math


# Display topology graph
# input：graph
def _show_topology_graph(graph):
    pos = nx.spring_layout(graph, iterations=200) 
    nx.draw(graph, pos, with_labels=True)
    labels = nx.get_edge_attributes(graph, 'link_id')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels,label_pos=0.6)
    #plt.show(block=False)
    plt.show()
    # plt.pause(10)
    # plt.close('all')

# Generate tree topology
# input：the number of switches，the number of end station of each switch
# output：topology, end station id set
def _generate_tree_topo_graph(sw_num,
                                es_num_per_sw_set,
                                show_topo_graph):
    
    G = nx.DiGraph()

    # step1，add all the switch nodes
    sw_id = 0
    for sw in range(sw_num):
        G.add_node(sw_id, node_id=sw_id, node_type='SW', es_set=[])
        sw_id += 1

    # step2，add links between switches
    sw_id_set = range(0, sw_num)
    link_id = 0
    for sw in sw_id_set[1:]:
        #find target_sw
        layer=int(math.log2(sw+1))
        target_sw=int(math.ceil((sw+2-math.pow(2,layer))/2)+math.pow(2,layer-1)-2)
        G.add_edge(sw, target_sw, link_id=link_id)
        link_id += 1
        G.add_edge(target_sw, sw, link_id=link_id)
        link_id += 1

    #step3，add end station nodes
    es_id_set=[]
    es_id = sw_num
    for sw in range(sw_num):
        es_num_of_current_sw = choice(es_num_per_sw_set)
        for es in range(es_num_of_current_sw):
            G.add_node(es_id, node_id=es_id, node_type='ES')
            es_id_set.append(es_id)
            # find the connected switch
            es_set = G.nodes[sw]['es_set']#dictionary of sw node
            es_set.append(es_id)
            G.nodes[sw]['es_set'] = es_set
            es_id += 1

    #step4，add the links between switches and end stations
    for sw in sw_id_set:
        es_set = G.nodes[sw]['es_set']
        print(es_set)
        for es in es_set:
            G.add_edge(sw, es, link_id=link_id)
            link_id += 1
            G.add_edge(es, sw, link_id=link_id)
            link_id += 1

    # show the topologies
    if show_topo_graph:
        _show_topology_graph(G)

    print(G)

    return G,es_id_set
    


# generate ring topology graph
# input：the number of switches，the number of end station of each switch
# output：topology, end station id set
def _generate_ring_topo_graph(sw_num,
                                es_num_per_sw_set,
                                show_topo_graph):

    
    G = nx.DiGraph()

    # step1，add all the switch nodes
    sw_id = 0
    for sw in range(sw_num):
        G.add_node(sw_id, node_id=sw_id, node_type='SW', es_set=[])
        sw_id += 1

    # step2，add links between switches
    sw_id_set = range(0, sw_num)
    link_id = 0
    for sw in sw_id_set[0:-1]:
        G.add_edge(sw, sw + 1, link_id=link_id)
        link_id += 1
        G.add_edge(sw + 1, sw, link_id=link_id)
        link_id += 1

    G.add_edge(sw_id_set[-1],sw_id_set[0],link_id=link_id)
    link_id+=1
    G.add_edge(sw_id_set[0],sw_id_set[-1],link_id=link_id)
    link_id+=1

    #step3，add end station nodes
    es_id_set=[]
    es_id = sw_num
    for sw in range(sw_num):
        es_num_of_current_sw = choice(es_num_per_sw_set)
        for es in range(es_num_of_current_sw):
            G.add_node(es_id, node_id=es_id, node_type='ES')
            es_id_set.append(es_id)
            # find the connected switch
            es_set = G.nodes[sw]['es_set']#dictionary of sw node
            es_set.append(es_id)
            G.nodes[sw]['es_set'] = es_set
            es_id += 1

    #step4，add the links between switches and end stations
    for sw in sw_id_set:
        es_set = G.nodes[sw]['es_set']
        print(es_set)
        for es in es_set:
            G.add_edge(sw, es, link_id=link_id)
            link_id += 1
            G.add_edge(es, sw, link_id=link_id)
            link_id += 1

    # show the topologies
    if show_topo_graph:
        _show_topology_graph(G)

    print(G)

    return G,es_id_set



# generate linear topology graph
# input：the number of switches，the number of end station of each switch
# output：topology, end station id set
def _generate_linear_topo_graph(sw_num,
                                es_num_per_sw_set,
                                show_topo_graph):

    G = nx.DiGraph()

   # step1，add all the switch nodes
    sw_id = 0
    for sw in range(sw_num):
        G.add_node(sw_id, node_id=sw_id, node_type='SW', es_set=[])
        sw_id += 1

    #step2，add end station nodes
    es_id_set=[]
    es_id = sw_num
    for sw in range(sw_num):
        es_num_of_current_sw = choice(es_num_per_sw_set)
        for es in range(es_num_of_current_sw):
            G.add_node(es_id, node_id=es_id, node_type='ES')
            es_id_set.append(es_id)
            # find the connected switch
            es_set = G.nodes[sw]['es_set']#dictionary of sw node
            es_set.append(es_id)
            G.nodes[sw]['es_set'] = es_set
            es_id += 1

    # step3，add links between switches
    sw_id_set = range(0, sw_num)
    link_id = 0
    for sw in sw_id_set[0:-1]:
        G.add_edge(sw, sw + 1, link_id=link_id)
        link_id += 1
        G.add_edge(sw + 1, sw, link_id=link_id)
        link_id += 1

    #step4，add the links between switches and end stations
    for sw in sw_id_set:
        es_set = G.nodes[sw]['es_set']
        print(es_set)
        for es in es_set:
            G.add_edge(sw, es, link_id=link_id)
            link_id += 1
            G.add_edge(es, sw, link_id=link_id)
            link_id += 1

    # show the topologies
    if show_topo_graph:
        _show_topology_graph(G)

    print(G)
    return G,es_id_set


# generate topology
def _generate_topology(sw_num,
                       es_num_per_sw_set,
                       topo_type,
                       **kwargs  # show_topo_graph
                       ):
    # parse kwargs
    if kwargs.get('show_topo_graph') is None:
        show_topo_graph = False
    else:
        show_topo_graph = kwargs['show_topo_graph']

    G = None
    topo_set = []
    if topo_type =='linear':
        G ,es_id_set= _generate_linear_topo_graph(sw_num, es_num_per_sw_set, show_topo_graph)
    elif topo_type=='ring':
        G, es_id_set=_generate_ring_topo_graph(sw_num,es_num_per_sw_set,show_topo_graph)
    elif topo_type=='tree':
        G,es_id_set=_generate_tree_topo_graph(sw_num,es_num_per_sw_set,show_topo_graph)
    else:
        print('Error - invalid topo_type')
        exit(0)

    links = G.edges
    for per_link in links:
        src_node = per_link[0]
        dst_node = per_link[1]
        link_id = G[src_node][dst_node]['link_id']
        link = {}
        link = {'link_id': link_id, 'src_node': src_node,
                    'dst_node': dst_node
                    }
        topo_set.append(link)
    topo_set.sort(key=lambda x: x['link_id'])
    return G, topo_set,es_id_set


#generate flows/streams
def _generate_random_streams(G,
                            es_id_set,
                            flow_num,
                            size_set,
                            period_set,
                            latency_requirement_set):
    
    #generate all the possible src-dst
    src_dst_set=[]
    for src_id in es_id_set:
        dst_id_set=copy.deepcopy(es_id_set)
        dst_id_set.remove(src_id)
        for dst_id in dst_id_set:
            src_dst_set.append((src_id,dst_id))
    #print(src_dst_set,len(src_dst_set))

    #generate all the possible flows
    all_flow=[]
    flow_id=0
    for (src,dst) in src_dst_set:
        path_length=nx.shortest_path_length(G,source=src,target=dst)
        #traverse all the possible periods
        for period in period_set:
            if period>=path_length:
                max_num=period-path_length+1
                for num_id in range(max_num):
                    flow = {'flow_id': flow_id,
                            'src':src,
                            'dst':dst,
                            'size': size_set[0],
                            'period': period,
                            'ddl': latency_requirement_set[0]}
                    all_flow.append(flow)
                    flow_id+=1
    
    print("all flow:",len(all_flow))

    #radomly choose flows
    sample_flow_id=random.sample(range(0,len(all_flow)),flow_num)
    print(sample_flow_id)

    sample_flow_set=[]
    for i in sample_flow_id:
        flow_copy=copy.deepcopy(all_flow[i])
        sample_flow_set.append(flow_copy)

    for flow in sample_flow_set:
        
        #print(flow,sample_flow_set.index(flow))
        flow['flow_id']=sample_flow_set.index(flow)


    return sample_flow_set







# generate topologies and flows according to requirements and write to txt files

def construct_topo_and_frames(topo_txt,
                               stream_txt,
                               topo_type='ring',
                               sw_num=5,
                               es_num_per_sw_set=None,
                               flow_num=50,
                               size_set=None,
                               period_set=None,
                               latency_requirement_set=None,
                               **kwargs):  # show_topo_graph
    if es_num_per_sw_set is None:
        es_num_per_sw_set = [2]
    
    if size_set is None:
        size_set = [1518]
    if period_set is None:
        period_set = [20000]
    if latency_requirement_set is None:
        latency_requirement_set = [20000]

    # step1, generate topology
    G, topo_set ,es_id_set= _generate_topology(sw_num,
                                     es_num_per_sw_set,
                                     topo_type,
                                     **kwargs
                                     )
    #print("end_node_set",es_id_set)

    # step2：write topology to txt
    write_topo_or_stream_to_txt(topo_txt, topo_set)

    
    # step3：generate flows/streams
    flow_set=_generate_random_streams(G,
                                es_id_set,
                                flow_num,
                                size_set,
                                period_set,
                                latency_requirement_set)
    
    # step4: write flows to txt
    write_topo_or_stream_to_txt(stream_txt, flow_set)

    return


def _main():
    construct_topo_and_frames('./data/topo.txt',#the path of the output topology txt
                               './data/flow.txt',#the path of the ouput flow txt
                               topo_type='ring',
                               sw_num=4,
                               es_num_per_sw_set=[2],
                               flow_num=150,
                               size_set=[1518],
                               period_set=[2,4,8,16],
                               latency_requirement_set=[20],
                               show_topo_graph=True)
    return


if __name__ == '__main__':
    _main()
