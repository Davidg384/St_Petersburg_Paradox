// ConsoleApplication1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <stdlib.h>
#include <ctime>
#include <fstream>
#include <string>

using namespace std;


int coin_flip() {
	/* This function returns either 0 or 1. 
	Here 0 is a coin flip of tails and heads is 1*/
	return rand() % 2;
}


double sp() {
	/*This function is 1 Saint Petersburg game.
	The coin keeps being flipped until heads is landed.
	Then 2^n is returned, where n is the number of flips
	that it took to get heads.*/
	int n = 1; 
	int flip = 0;
	while(flip == 0) {
		n++;
		flip = coin_flip();
	}
	return pow(2,n);
}

double buffon() {
	double summation = 0;
	for (int spcount = 0; spcount < 2048; spcount++) {
		summation += sp();
	}
	return summation / 2048;
}

int main() {
	srand(time(NULL));
	ofstream outputFile;
	outputFile.open("averages.txt");
	int n = 1000000;
	for (int i = 0; i < n; i++) {
		outputFile << buffon() << endl;
	}
	outputFile.close();
}