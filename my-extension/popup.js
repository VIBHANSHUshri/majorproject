document.getElementById("checkButton").addEventListener("click", function() {
    var url = document.getElementById("gifUrl").value;
    var resultDiv = document.getElementById("result");
    resultDiv.textContent = "Checking...";
  
    fetch("http://localhost:5000/check-gif-url", {
      method: "POST",   
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
      resultDiv.textContent = data.message;
    })
    .catch(error => {
      resultDiv.textContent = "Error checking GIF. Please try again.";
    });
  });
  