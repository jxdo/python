# coding:gbk
__author__ = 'Administrator'

#  最短路径算法
class DijkstraExtendPath():
    def __init__(self, node_map):
        self.node_map = node_map
        self.node_length = len(node_map)
        self.used_node_list = []
        self.collected_node_dict = {}
    def __call__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self._init_dijkstra()
        return self._format_path()
    def _init_dijkstra(self):
        self.used_node_list.append(self.from_node)
        self.collected_node_dict[self.from_node] = [0, -1]
        for index1, node1 in enumerate(self.node_map[self.from_node]):
            if node1:
                self.collected_node_dict[index1] = [node1, self.from_node]
        self._foreach_dijkstra()
    def _foreach_dijkstra(self):
        if len(self.used_node_list) == self.node_length - 1:
            return
        for key, val in self.collected_node_dict.items():  # 遍历已有权值节点
            if key not in self.used_node_list and key != to_node:
                self.used_node_list.append(key)
            else:
                continue
            for index1, node1 in enumerate(self.node_map[key]):  # 对节点进行遍历
                # 如果节点在权值节点中并且权值大于新权值
                if node1 and index1 in self.collected_node_dict and self.collected_node_dict[index1][0] > node1 + val[0]:
                    self.collected_node_dict[index1][0] = node1 + val[0] # 更新权值
                    self.collected_node_dict[index1][1] = key
                elif node1 and index1 not in self.collected_node_dict:
                    self.collected_node_dict[index1] = [node1 + val[0], key]
        self._foreach_dijkstra()
    def _format_path(self):
        node_list = []
        temp_node = self.to_node
        node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        while self.collected_node_dict[temp_node][1] != -1:
            temp_node = self.collected_node_dict[temp_node][1]
            node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        node_list.reverse()
        return node_list
def set_node_map(node_map, node, node_list):
    for x, y, val in node_list:
        node_map[node.index(x)][node.index(y)] = node_map[node.index(y)][node.index(x)] =  val
if __name__ == "__main__":
    node = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20', '21', '22', '23', '24', '25', '26']    # 计算用到的节点
    node_list = [['1', '2', 100], ['2', '3', 87], ['2', '4', 57], ['2', '5', 50], ['2', '6', 51],
                 ['3', '7', 94],  ['3', '8', 78], ['3', '9', 85], ['4', '13', 54], ['4', '14', 47],
                 ['4', '15', 98], ['5', '10', 43], ['5', '11', 32], ['5', '12', 44], ['6', '16', 59],
                 ['6', '17', 92], ['6', '18', 39], ['6', '23', 99], ['7', '19', 99], ['8', '20', 96],
                 ['9', '20', 86], ['10', '21', 60], ['11', '21', 57], ['12', '22', 47], ['14', '10', 55],
                 ['16', '17', 59], ['18', '12', 53], ['18', '24', 93], ['21', '22', 33], ['19', '25', 88],
                 ['20', '25', 96], ['22', '25', 23], ['25', '26', 75]]        # 计算用到的所有节点之间的路径
    node_map = [[0 for val in xrange(len(node))] for val in xrange(len(node))]
    set_node_map(node_map, node, node_list)
    # A -->; D
    from_node = node.index('1')
    to_node = node.index('26')
    dijkstrapath = DijkstraExtendPath(node_map)
    path = dijkstrapath(from_node, to_node)
    print path