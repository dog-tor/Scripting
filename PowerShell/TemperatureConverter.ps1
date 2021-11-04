# Name: dog-tor
# Convert temperature to and from Celsius and Fahrenheit.

$Choices = @('1','y','Y','0','n','N') # Create two arrays for the available choices.
$YesChoices = @('1','y','Y')
$Continue = 1 # Set the value to begin the While loop.

While ($Continue -in $YesChoices) {

    Write-Output "`n`t`tTemperature Converter"
    Write-Output "======================================="
    Write-Output "1. Celsius to Fahrenheit"
    Write-Output "2. Fahrenheit to Celsius"
    $Option = Read-Host "Select Option"

    if ($Option -eq 1) { # Do the following if option 1 is entered.

        [double]$C = Read-Host "`nWhat is the temperature in Celsius"
        $F=$C*9/5+32 # Perform the conversion operation on the entered value.

        Write-Output "Celsius $C is Fahrenheit $F"

        $Continue = Read-Host "`nDo you want to continue? (y/Y or 1 = yes, n/N or 0 = no)"
        
        while ($Continue -notin $Choices) { # Another loop to require the correct input

            Write-Output "Invalid option. Please enter any of the allowed options."
            $Continue = Read-Host "`nDo you want to continue? (y/Y or 1 = yes, n/N or 0 = no)"

        }
    }elseif ($Option -eq 2){ # Do the following if option 2 is entered.

        [double]$F = Read-Host "`nWhat is the temperature in Fahrenheit"
        $C=($F-32)*5/9 # Perform the conversion operation on the entered value.

        Write-Output "Fahrenheit $F is Celsius $C"

        $Continue = Read-Host "`nDo you want to continue? (y/Y or 1 = yes, n/N or 0 = no)"
        
        while ($Continue -notin $Choices) { # Another loop to require the correct input

            Write-Output "Invalid option. Please enter any of the allowed options."
            $Continue = Read-Host "`nDo you want to continue? (y/Y or 1 = yes, n/N or 0 = no)"
        }

    }else { # Prompt the user to select the require options.

        echo "`nWrong option. Please enter 1 or 2.`n"
    }
}

# Print this message once the loop is exited.
Write-Output "`nThank you, Bye!"
