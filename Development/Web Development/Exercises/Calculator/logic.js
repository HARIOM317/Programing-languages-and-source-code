function display(number) {
    document.getElementById("result").value += number;

}

function ans() {
    var myResult = document.getElementById("result").value;
    var value = eval(myResult);
    document.getElementById("result").value = value;
}

function clear_screen() {
    document.getElementById("result").value = "";
}

function square() {
    var number = document.getElementById("result").value;
    result = number * number;
    document.getElementById("result").value = result;
}