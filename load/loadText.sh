#! /bin/bash

outputDirName=$1

outputDestination=$2

# Create directory to store transformed data file(s)
mkdir $outputDirName

# Move transformed data into the directory
mv gameData.* $outputDirName

# Move data to the destination
mv $outputDirName $outputDestination