#include<iostream>
#include<fstream>
#include<queue>
#include<vector>

using namespace std;


int main() {
	ifstream in("huffman.in");
	int size;
	in >> size;

	vector<long long> vec;
	long long elem;
	for (int i = 0; i < size; i++) {
		in >> elem;
		vec.push_back(elem);
	}
	in.close();

	std::priority_queue<long long, std::vector<long long >, std::greater<>> q(vec.begin(), vec.end());

	long long result = 0;
	while (q.size() != 1) {
		long long sum = 0;
		sum += q.top();
		q.pop();
		sum += q.top();
		result += sum;
		q.push(sum);
		q.pop();
	}

	ofstream out("huffman.out");
	out << result;
	out.close();
	return 0;
}