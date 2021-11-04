# Name: dog-tor
# Read a file name in the test_users directory and print its contents to the user.
# 
# Read the file name with the pattern firstname_lastname.usr.
$FileName = Read-Host "Enter the file name with the pattern firstname_lastname.usr"

# Read the file entered from the test_users directory.
$UserData = Get-Content test_users\$FileName

# Echo the user's information from the file name entered.
echo $UserData