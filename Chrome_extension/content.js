// Create the button element
if(document.body)
{
  process();
  fnDefineEvents();
  //addText();
}
else 
{
  document.addEventListener('DOMContentLoaded', process);
  document.addEventListener('DOMContentLoaded', fnDefineEvents);
}

function process() 
{
  var btn = document.createElement("input");
  btn.value = "Evaluate";
  btn.type= "submit";
  btn.id="eval_btn";
  str="results?search_query";
    
  
  //Add an event listener to the button
  /*if(window.location.toString().includes("results"))
  {
    button.addEventListener("click", function() {
      alert("Show Positivity Percentage");
    });
  }*/
  console.log("Hello");
  // Add the button to the page
  var voicebtn = document.getElementById("voice-search-button");
  voicebtn.parentNode.appendChild(btn);
}

function fnDefineEvents(){
  // Add an event listener to the button

document.getElementById("eval_btn").addEventListener("click", function(event) {
  addText();
});
}

function addText(){
  var title=document.getElementsByClassName("yt-simple-endpoint style-scope ytd-video-renderer");
  console.log(title.length);
  for(let i=0;i<title.length/2;i++)
  {
    title[i*2].innerHTML=title[i*2].textContent+ " Hello"+ i.toString();
  }
  //title=title+" "+ "Hello";
  //document.getElementById("video-title").innerHTML=title;
  
}





