// codeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <stddef.h>
#include <sstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	//
	//INPUT BEGIN
	//

	fstream data;
	data.open("A-small-attempt4.in");

	ofstream results;
	results.open("results.txt");


	int n = 0;
	string number_str;
	getline(data,number_str);
	stringstream convert(number_str);
	convert >> n;

	int counter = 0;
	while(counter < n)
	{
		counter++;


	char grid[4][4];
	for(int i = 0; i <= 3; i++)
	{
		string line;
		getline(data,line);
		for(int j = 0; j <= 3; j++)
		{
			grid[i][j] = line.at(j);
		}
	}

	getline(data,number_str);

	//
	//INPUT END
	//

	bool X_WIN = false;
	bool O_WIN = false;
	bool DRAW = false;
	bool NOT_COMPLETE = false;


	for(int i = 0; i <= 3; i++) 
	{
		string line;
		line += grid[i][0];
		line += grid[i][1];
		line += grid[i][2];
		line += grid[i][3];
		
		int count_X = 0;
		int count_T = 0;
		int count_O = 0;

		for (int i = 0; i < line.size(); i++)
			if (line[i] == 'X') count_X++;

		for (int i = 0; i < line.size(); i++)
			if (line[i] == 'T') count_T++;

		for (int i = 0; i < line.size(); i++)
			if (line[i] == 'O') count_O++;

		if(count_X == 4 || (count_X == 3 && count_T == 1))
		{
			X_WIN = true;
		}
		if(count_O == 4 || (count_O == 3 && count_T == 1))
		{
			O_WIN = true;
		}
	}

	for(int i = 0; i <= 3; i++) 
	{
		string line;
		line += grid[0][i];
		line += grid[1][i];
		line += grid[2][i];
		line += grid[3][i];
		
		int count_O = 0;
		int count_T = 0;
		int count_X = 0;

		for (int i = 0; i < line.size(); i++)
			if (line[i] == 'O') count_O++;

		for (int i = 0; i < line.size(); i++)
			if (line[i] == 'T') count_T++;

		for (int i = 0; i < line.size(); i++)
			if (line[i] == 'X') count_X++;

		if(count_O == 4 || (count_O == 3 && count_T == 1))
		{
			O_WIN = true;
		}
		if(count_X == 4 || (count_X == 3 && count_T == 1))
		{
			X_WIN = true;
		}
	}




	string line;
	line += grid[0][0];
	line += grid[1][1];
	line += grid[2][2];
	line += grid[3][3];
		
	int count_X = 0;
	int count_T = 0;
	int count_O = 0;

	for (int i = 0; i < line.size(); i++)
		if (line[i] == 'X') count_X++;

	for (int i = 0; i < line.size(); i++)
		if (line[i] == 'O') count_O++;

	for (int i = 0; i < line.size(); i++)
		if (line[i] == 'T') count_T++;

	if(count_X == 4 || (count_X == 3 && count_T == 1))
	{
		X_WIN = true;
	}

	if(count_O == 4 || (count_O == 3 && count_T == 1))
	{
		O_WIN = true;
	}

	line = "";
	line += grid[0][3];
	line += grid[1][2];
	line += grid[2][1];
	line += grid[3][0];
		
	count_X = 0;
	count_T = 0;
	count_O = 0;

	for (int i = 0; i < line.size(); i++)
		if (line[i] == 'X') count_X++;

	for (int i = 0; i < line.size(); i++)
		if (line[i] == 'O') count_O++;

	for (int i = 0; i < line.size(); i++)
		if (line[i] == 'T') count_T++;

	if(count_X == 4 || (count_X == 3 && count_T == 1))
	{
		X_WIN = true;
	}

	if(count_O == 4 || (count_O == 3 && count_T == 1))
	{
		O_WIN = true;
	}




	if(X_WIN == false && O_WIN == false)
	{
		DRAW = true;
		string line;
		for(int i = 0; i <= 3; i++)
		{
			for(int j = 0; j <= 3; j++)
			{
				line += grid[i][j];
			}
		}

		if(line.find(".") != string::npos)
		{
			DRAW = false;
			NOT_COMPLETE = true;
		}
	}





	if(X_WIN)
		results << "Case #" << counter << ": X won" << '\n';
	if(O_WIN)
		results << "Case #" << counter << ": O won" << '\n';
	if(DRAW)
		results << "Case #" << counter << ": Draw" << '\n';
	if(NOT_COMPLETE)
		results << "Case #" << counter << ": Game has not completed" << '\n';


	}

	string line;
	cin >> line;

	data.close();
	results.close();

	return 0;
}

