#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

struct Node {
	long long key;
	Node* left;
	Node* right;
};

void search(Node* root, long long x) {
	if (root != NULL) {
		if (root->key == x) {
			cout << root->key << endl;
			cout << root->right->key << endl;
			cout << root->left->key << endl;
			return;
		}
		else {
			search(root->left, x);
			search(root->right, x);
		}
	}
}

void addNode(long long x, Node*& root) {
	if (root == NULL) { 
		root = new Node; 
		root->key = x;   
		root->left = NULL;
		root->right = NULL;
	}
	else if(x == root->key){
		return;
	}
	else  if (x < root->key)   
		addNode(x, root->left);
	else
		addNode(x, root->right);
}

void printTree(Node* tree, vector<long long>& array) {
	if (tree != NULL) {
		array.push_back(tree->key);
		printTree(tree->left, array);
		printTree(tree->right, array);
	}
}

int main() {
	ifstream in;
	in.open("input.txt");
	long number;
	vector<long long> numbers;

	while (in >> number) {
		numbers.push_back(number);
	}
	in.close();

	Node* root = NULL;
	for (int i = 0; i < numbers.size(); i++) {
		addNode(numbers[i], root);
	}

	search(root, 2);

	vector<long long> nodes;
	printTree(root, nodes);
	ofstream out;
	out.open("output.txt");

	for (int i = 0; i < nodes.size(); i++) {
		out << nodes[i];
		if (i != nodes.size() - 1) {
			out << endl;
		}
	}
	out.close();
	return 0;
}