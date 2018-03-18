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

function checkPassword() 
{
  var numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];
  var password = document.getElementById("pw").value.toLowerCase();
  var num1 = 0;
  var num3 = 1;
  var finals = "";
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
  
  if (num3 == false)
  {
    finals+="Your password successfully contains a number.";
  }
  else
  {
    finals+="Your password must contain a number.";
  }
  
  if (num1 == true)
  {
    finals+=" Your password is a dictionary word.";
  }
  else
  {
    finals+=" Your password is not a dictionary word.";
  }
  
  
  //place your code here
  if (password.length >= 7 && password.length < 12)
  {
    finals+=" Your password is long enough.";
  }
  else
  {
    finals+=" Your password length is insufficient.";
  }
  
  var apple = password.charAt(password.length-1);
  if (apple == '!' || apple == '@' || apple == '#' || apple == '$' || apple == '%' || apple =='*')
  {
    finals+=" Your password ends with a special character.";
  }
  else
  {
    finals+=" Your password does not end with a special character.";
  }
  //end your code here
  document.getElementById("results").innerHTML = finals;
}


