# Name: dog-tor
# Read input data and print it to the user.
# 
# Read the data from the user.
$FullName = Read-Host "Enter User’s Full Name `t`t: <Enter a first name B last name; alpha and space only>"
$UserID = Read-Host "Enter User’s ID `t`t`t: <Enter a 6 digit number; digits only>"
$JobLocation = Read-Host "Enter User’s Job Location `t: <Enter 4 characters> `n`t`t`t`t`t`t`t  [Make sure to enter AA99 pattern job location, eg: BX56, CR91]"
$ManagerCode = Read-Host "Enter User’s Manager Code `t: <Enter a 6 digit number; digits only>"

# Write the data to the console.
Write-Host "`n`nUser’s Full Name `t: $FullName"
Write-Host "User’s ID `t`t`t: $UserID"
Write-Host "User’s Job Location : $JobLocation"
Write-Host "User’s Manager Code : $ManagerCode"