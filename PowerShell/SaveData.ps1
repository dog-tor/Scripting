# Name: dog-tor
# Read input data, print it to the user, and save it to a file.
# 
# Read the data from the user.
$FullName = Read-Host "Enter User’s Full Name `t`t: <Enter a first name B last name; alpha and space only>"
$UserID = Read-Host "Enter User’s ID `t`t`t: <Enter a 6 digit number; digits only>"
$JobLocation = Read-Host "Enter User’s Job Location `t: <Enter 4 characters> `n`t`t`t`t`t`t`t  [Make sure to enter AA99 pattern job location, eg: BX56, CR91]"
$ManagerCode = Read-Host "Enter User’s Manager Code `t: <Enter a 6 digit number; digits only>"

# Set the file name with the pattern firstname_lastname.usr.
$FileName = "$FullName.usr" -Replace " ","_"

# Create the file to Save the data to.
New-Item test_users\$FileName

# Write the data to the console and the file by piping the output 
# to a file name with the pattern firstname_lastname.usr.
Write-Output "`n`nUser’s Full Name `t: $FullName" | Out-File test_users\$FileName -Append
Write-Output "User’s ID `t`t`t: $UserID" | Out-File test_users\$FileName -Append
Write-Output "User’s Job Location : $JobLocation" | Out-File test_users\$FileName -Append
Write-Output "User’s Manager Code : $ManagerCode" | Out-File test_users\$FileName -Append