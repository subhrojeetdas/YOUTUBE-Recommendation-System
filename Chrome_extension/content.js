// Create the button element
if(document.body)
{
  process();
}
else 
{
  document.addEventListener('DOMContentLoaded', process);
}
function process() 
{
  var button = document.createElement("button");
  button.innerHTML = "My Button";
  str="results?search_query";
  // Add an event listener to the button
  if(window.location.toString().includes("results"))
  {
    button.addEventListener("click", function() {
      alert("Show Positivity Percentage");
    });
  }
  console.log("Hello");
  // Add the button to the page
  var voicebtn = document.getElementById("search-form");
  voicebtn.parentNode.insertBefore(button, voicebtn);
}
/*// Create the button element
var button = document.createElement("button");
button.innerHTML = "My Button";

// Add an event listener to the button
button.addEventListener("click", function() {
  alert("Button was clicked!");
});

// Add the button to the page
var voicebtn = document.getElementById("voice-search-button");
voicebtn.parentNode.insertAfter(button, voicebtn);*/


