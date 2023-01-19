#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

struct Node {
	long long key;
	Node* left;
	Node* right;
};

void addNode(long long x, Node*& root) {
	if (root == NULL) {
		root = new Node;
		root->key = x;
		root->left = NULL;
		root->right = NULL;
	}
	else if (x == root->key) {
		return;
	}
	else  if (x < root->key)
		addNode(x, root->left);
	else
		addNode(x, root->right);
}

struct Node* findMin(Node* node) {
	if (node->left != NULL) {
		return findMin(node->left);
	}
	else {
		return node;
	}
}

struct Node* deleteNode(long long x, Node* root) {
	if (root == NULL) {
		return NULL;
	}
	else if (x < root->key) {
		root->left = deleteNode(x, root->left);
		return root;
	}
	else if (x > root->key) {
		root->right = deleteNode(x, root->right);
		return root;
	}
	else {
		if (root->left == NULL) {
			return root->right;
		}
		else if (root->right == NULL) {
			return root->left;
		}
		else {
			long long min_key = findMin(root->right)->key;
			root->key = min_key;
			root->right = deleteNode(min_key, root->right);
		}
		return root;
	}
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
	long long numberToDelete;
	long number;
	vector<long long> numbers;

	in >> numberToDelete;
	while (in >> number) {
		numbers.push_back(number);
	}
	in.close();

	Node* root = NULL;
	for (int i = 0; i < numbers.size(); i++) {
		addNode(numbers[i], root);
	}

	root = deleteNode(numberToDelete, root);

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