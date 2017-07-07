var wordsList = [];

function init() 
{
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) 
  {
    document.getElementById("btnSubmit").disabled = true; 
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false; 
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() 
{
	var numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];
 	var password = document.getElementById("pw").value.toLowerCase();
 	var num1 = 0;
 	var num2 = 0;
 	var num3 = 1;
 	//num1 = dictionary word
 	//num2= not long enough
 	//num3= no number

  //checks dictionary
 	for(var x = 0; x < wordsList.length; x++)
 	{
        if (password == wordsList[x])
 		{
 			num1= 1;
 			x = wordsList.length;
 			document.getElementById("results").innerHTML = "Nope.";
 		}
 	}

  //checks length
  if (password.length < 12)
  {
    num2 = 1;
  }


 	//checks for number
 	for(var y = 0; y < numbers.length; y++) 
  {
    for(var w = 0; w < password.length; w++)
    {
      var char_letter = password.charAt(w);
      if (char_letter == numbers[y])
      {
        num3 = 0;
        w = password.length;
        y = numbers.length;
      }
    }
  }

  var final = "That works!";

  //num1, num2, num3 == 0
  //num1, num2, num3 == 1
  //num1, num2 == 1 & num3 == 0
  //num1, num3 == 1 & num2 == 0
  //num2, num3 == 1 & num1 == 0
  //num1 == 1
  //num2 == 1
  //num3 == 1

 	if (num1 == 0 && num2 == 0 && num3 == 0)
 	{
 		finals = "That works!";
 	}
  else if (num1 == 1 && num2 == 1 && num3 == 1)
  {
    finals = "Your password does not have any numbers, is not long enough, and contains a dictionary word."
  }
  else if (num1 == 1 && num2 == 1)
  {
    finals = "Your password contains a dictionay word, and is too short."
  }
  else if (num1 == 1 && num3 == 1)
  {
    finals = "Your password contains a dictionary word, and does not have any numbers."
  }
  else if (num2 == 1 && num3 == 1)
  {
    finals = "Your password is too short, and does not have any numbers."
  }
  else if (num1 == 1)
  {
    finals = "Your password contains a dictionary word."
  }
  else if (num2 == 1)
  {
    finals = "Your password is too short."
  }
  else if (num3 == 1)
  {
    finals = "Your password doesn't have any numbers."
  }
  document.getElementById("results").innerHTML = finals;
}



