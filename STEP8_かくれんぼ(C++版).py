#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void dfs(int node, int parent, vector<vector<int>> &graph, vector<int> &dist) {
 for (int next_node : graph[node]) {
  if (next_node == parent) continue;
  dist[next_node] = dist[node] + 1;
  dfs(next_node, node, graph, dist);
 }
}
int main() {
 int n, m;
 cin >> n >> m;
 vector<vector<int>> graph(n);
 for (int i = 0; i < m; i++) {
  int a, b;
  cin >> a >> b;
  a--;
  b--;
  graph[a].push_back(b);
  graph[b].push_back(a);
 }

// 頂点0から一番遠い頂点を探す
 vector<int> dist_from0(n, 0);
 dfs(0, -1, graph, dist_from0);
 std::vector<int>::iterator farthest_node_from0_value = std::max_element(dist_from0.begin(), dist_from0.end());
 int farthest_node_from0 = std::distance(dist_from0.begin(), farthest_node_from0_value);

// 頂点0から一番遠い頂点、から一番遠い頂点を探す
 vector<int> dist(n, 0);
 dfs(farthest_node_from0, -1, graph, dist);
 cout << *std::max_element(dist.begin(), dist.end());
}
