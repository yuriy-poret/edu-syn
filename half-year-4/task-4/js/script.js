function isValidNumber(str) {
    return /^-?\d+([,.]\d+)?$/.test(str);
}

function calculate(operation) {
    const input1    = document.getElementById('num1').value;
    const input2    = document.getElementById('num2').value;
    const resultDiv = document.getElementById('result');

    if (!isValidNumber(input1) || !isValidNumber(input2)) {
        resultDiv.textContent = 'Ошибка: введите корректные числа!';
        resultDiv.classList.add('error');
        return;
    }

    const num1 = parseFloat(input1.replace(',', '.'));
    const num2 = parseFloat(input2.replace(',', '.'));

    if (isNaN(num1) || isNaN(num2)) {
        resultDiv.textContent = 'Ошибка: введите корректные числа!';
        resultDiv.classList.add('error');
        return;
    }

    let result;

    switch (operation) {
        case 'sum':
            result = num1 + num2;
            break;
        case 'difference':
            result = num1 - num2;
            break;
        case 'product':
            result = num1 * num2;
            break;
        case 'division':
            if (num2 === 0) {
                resultDiv.textContent = 'Ошибка: деление на ноль!';
                resultDiv.classList.add('error');
                return;
            }
            result = num1 / num2;
            break;
        default:
            result = 'Неизвестная операция';
            break;
    }

    resultDiv.textContent = `Результат: ${result}`;
    resultDiv.classList.remove('error');
}
