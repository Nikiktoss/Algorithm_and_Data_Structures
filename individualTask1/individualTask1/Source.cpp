#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cmath>

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

void countNumberOfNodes(Node* node, long long& number) {
	if (node != NULL) {
		number++;
		countNumberOfNodes(node->left, number);
		countNumberOfNodes(node->right, number);
	}
}

long long heightOfNode(Node* node)
{
	if (node == NULL)
		return 0;
	long long left, right;
	if (node->left != NULL) {
		left = heightOfNode(node->left);
	}
	else
		left = -1;
	if (node->right != NULL) {
		right = heightOfNode(node->right);
	}
	else
		right = -1;
	long long max = left > right ? left : right;
	return max + 1;

}

void findAverageNodes(Node* node, vector<long long>& nodes) {
	long long numberLeft = 0, numberRight = 0;
	if(node != NULL){
		countNumberOfNodes(node->left, numberLeft);
		countNumberOfNodes(node->right, numberRight);
		if (numberLeft == numberRight  && heightOfNode(node->right) != heightOfNode(node->left)) {
			nodes.push_back(node->key);
		}
		findAverageNodes(node->left, nodes);
		findAverageNodes(node->right, nodes);
	}
}

void printTree(Node* tree, vector<long long>& array) {
	if (tree != NULL) {
		array.push_back(tree->key);
		printTree(tree->left, array);
		printTree(tree->right, array);
	}
}

long long findNodeToDelete(vector<long long> array) {
	if (array.size() % 2 == 0) {
		return NULL;
	}
	else if (array.size() == 1) {
		return array[0];
	}
	else {
		return array[floor(array.size() / 2)];
	}
}

int main() {
	ifstream in;
	in.open("in.txt");
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

	vector<long long> correctNodes;
	findAverageNodes(root, correctNodes);
	sort(correctNodes.begin(), correctNodes.end());
	if (findNodeToDelete(correctNodes) != NULL) {
		deleteNode(findNodeToDelete(correctNodes), root);
	}

	vector<long long> nodes;
	printTree(root, nodes);
	ofstream out;
	out.open("out.txt");

	for (int i = 0; i < nodes.size(); i++) {
		out << nodes[i];
		if (i != nodes.size() - 1) {
			out << endl;
		}
	}
	out.close();
	return 0;
}