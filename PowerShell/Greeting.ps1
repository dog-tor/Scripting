# Name: dog-tor
# Print a greeting to the user, the current date, and the user logged into the system.
# 
# Print the greeting to the user.
Write-Host "Good Morning $env:USERNAME"

# Print the current date.
Write-Host "Now it is $(Get-Date)"

# Print the user currently logged into the computer.
Write-Host "User in machine $env:COMPUTERNAME is $env:USERNAME"