async function calcularBhaskara() {
  const a = document.getElementById('a').value;
  const b = document.getElementById('b').value;
  const c = document.getElementById('c').value;

  const response = await fetch('/bhaskara', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({a, b, c})
  });

  const data = await response.json();
  document.getElementById('resultado').innerText = "Resultado: " + data.resultado;
}
