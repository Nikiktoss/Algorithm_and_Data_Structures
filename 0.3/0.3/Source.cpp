#include<iostream>
#include<vector>
#include<fstream>
 
using namespace std;

struct nodeData {
	long long key;
	long long min_value;
	long long max_value;
};

int main() {
	ifstream in("bst.in");
	long long numberOfNodes;
	long long keyOfRoot;
	char rl;
	long long infoKey, lineParent;

	in >> numberOfNodes;
	in >> keyOfRoot;
	
	vector<nodeData> data;
	nodeData r = nodeData();
	r.key = keyOfRoot;
	r.max_value = INT_MAX;
	r.min_value = INT_MIN;
	data.push_back(r);
	
	while (in >> infoKey && in >> lineParent && in >> rl) {
		nodeData d = nodeData();
		d.key = infoKey;
		if (rl == 'R') {
			d.min_value = data[lineParent - 1].key;
			d.max_value = data[lineParent - 1].max_value;
		}
		else {
			d.max_value = data[lineParent - 1].key - 1;
			d.min_value = data[lineParent - 1].min_value;
		}

		if (d.key <= d.max_value && d.key >= d.min_value) {
			data.push_back(d);
		}
		else {
			break;
		}
	}
	in.close();

	ofstream out("bst.out");
	if (data.size() == numberOfNodes) {
		out << "YES";
	}
	else {
		out << "NO";
	}
	out.close();

	return 0;
}