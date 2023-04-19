let shape = "";
let validShape = false;

// Loop para solicitar a forma geométrica até que o usuário escolha uma opção válida
while (!validShape) {
  shape = prompt(
    "Escolha uma forma geométrica (retângulo, triângulo ou círculo):"
  ).toLowerCase();

  // Verifica se a opção escolhida é válida
  if (shape === "retângulo" || shape === "triângulo" || shape === "círculo") {
    validShape = true;
  } else {
    alert("Opção inválida, tente novamente.");
  }
}

let area = 0;

// Calcula a área com base na forma geométrica escolhida
switch (shape) {
  case "retângulo":
    let baseRetangulo = parseFloat(prompt("Informe a base do retângulo:"));
    let alturaRetangulo = parseFloat(prompt("Informe a altura do retângulo:"));

    // Verifica se os valores de entrada são válidos
    if (baseRetangulo > 0 && alturaRetangulo > 0) {
      area = baseRetangulo * alturaRetangulo;
    } else {
      alert("Valores inválidos, tente novamente.");
    }

    break;

  case "triângulo":
    let baseTriangulo = parseFloat(prompt("Informe a base do triângulo:"));
    let alturaTriangulo = parseFloat(prompt("Informe a altura do triângulo:"));

    // Verifica se os valores de entrada são válidos
    if (baseTriangulo > 0 && alturaTriangulo > 0) {
      area = (baseTriangulo * alturaTriangulo) / 2;
    } else {
      alert("Valores inválidos, tente novamente.");
    }

    break;

  case "círculo":
    let raio = parseFloat(prompt("Informe o raio do círculo:"));

    // Verifica se o valor de entrada é válido
    if (raio > 0) {
      area = 3.14 * raio ** 2;
    } else {
      alert("Valor inválido, tente novamente.");
    }

    break;
}

// Imprime o resultado no console
console.log(`A área do ${shape} é: ${area}`);
