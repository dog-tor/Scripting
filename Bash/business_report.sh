#!/bin/bash
#
# Name: dog-tor
# Print the contents of the business_performance.dat file in a formatted output.
#
# Print the header/banner.

printf "\n%24s %s\n" "" "Global Traders Inc"
printf "%-10s %-s\n" "" "Business Performance Report by Location/Business Area"
printf "\n%-17s %s\n" "" "Report Date $(date)"

printf "\n%-18s %11s %13s %11s %8s %17s\n" "Location" "Marketing" "Advertising" "Production" "I. Tech" "Total Revenue"
printf "%s\n" "..................................................................................."

# Check to see if the file already exists before printing its contents.
fileName="./business_performance.dat"
if [ ! -e "$fileName" ];
then
    echo "file : <$fileName> does not exist." # Print to the console if the file does not exist.
else
    
    # Set the default value for totals.
    total2=0
    total3=0
    total4=0
    total5=0
    totalTotal=0
	
    # Loop over each line in the file and assign each column to the following variables.
    while IFS=, read -r data1 data2 data3 data4 data5; do # Read each column if the file exists.
        
        # Calculate the total for the total column.    
	totalRev=$(echo "$data2+$data3+$data4+$data5" | bc -l)
	
	# Print the data in each column.
        printf "%-19s %10.2f %11.2f %12.2f %11.2f %12.2f\n" "$data1" "$data2" "$data3" "$data4" "$data5" "$totalRev"
	
        # Calculate the total for each column.
	total2=$(echo "$data2+$total2" | bc -l)
	total3=$(echo "$data3+$total3" | bc -l)
	total4=$(echo "$data4+$total4" | bc -l)
	total5=$(echo "$data5+$total5" | bc -l)
	totalTotal=$(echo "$totalRev+$totalTotal" | bc -l)

    # End the loop and close the file.
    done<"$fileName"

    printf "%s\n" "-----------------------------------------------------------------------------------"
    # Print the totals.
    printf "%-19s %10.2f %11.2f %12.2f %11.2f %12.2f\n" "Totals" "$total2" "$total3" "$total4" "$total5" "$totalTotal"
    printf "%s\n" "-----------------------------------------------------------------------------------"
    
    # Set the default value for each forecasted total.
    forecast2=3000000.00
    forecast3=2500000.00
    forecast4=400000.00
    forecast5=200000.00
    forecastTotal=7500000.00

    # Print the forecasted totals.
    printf "%-19s %10.2f %11.2f %12.2f %11.2f %12.2f\n" "Forecasted" "$forecast2" "$forecast3" "$forecast4" "$forecast5" "$forecastTotal"
    printf "%s\n" "-----------------------------------------------------------------------------------"
    
    # Calculate the Profit/Loss.
    profitLoss2=$(echo "$total2-$forecast2" | bc -l)
    profitLoss3=$(echo "$total3-$forecast3" | bc -l)
    profitLoss4=$(echo "$total4-$forecast4" | bc -l)
    profitLoss5=$(echo "$total5-$forecast5" | bc -l)
    profitLossTotal=$(echo "$totalTotal-$forecastTotal" | bc -l)
    
    # Print the Profit/Loss.
    printf "%-19s %10.2f %11.2f %12.2f %11.2f %12.2f\n" "Profit/Loss(-)" "$profitLoss2" "$profitLoss3" "$profitLoss4" "$profitLoss5" "$profitLossTotal"
    printf "%s\n" "-----------------------------------------------------------------------------------"

fi
