# Name: dog-tor
# Read a file name in the test_users directory and print its contents to the user.
# 
# Read the file name with the pattern firstname_lastname.usr.
$FileName = Read-Host "Enter the file name with the pattern firstname_lastname.usr"

# Read the file entered from the test_users directory if it exists.
if (Test-Path test_users\$FileName) {

$UserData = Get-Content test_users\$FileName

# Echo the user's information from the file name entered.
echo $UserData

}else {

# Echo a message if the entered file name does not exist in the test_users directory.
echo "file : <$FileName> does not exists"

}