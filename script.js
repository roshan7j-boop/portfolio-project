document.getElementById("contactForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const btn = document.querySelector("button");
  btn.innerText = "Sending...";

  const data = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    message: document.getElementById("message").value
  };

  const res = await fetch("http://localhost:5000/contact", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  const result = await res.json();

  btn.innerText = "Send Message";
  document.getElementById("response").innerText = result.message;
});
