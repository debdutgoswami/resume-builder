function addmore(){
    var table = document.getElementById("tb2");
    var row = table.insertRow(-1);
    var name = row.insertCell(0);
    var position = row.insertCell(1);
    var start = row.insertCell(2);
    var end = row.insertCell(3);
    var description = row.insertCell(4);

    name.innerHTML = "new name";
    position.innerHTML = "new position";
    start.innerHTML = "new start";
    end.innerHTML = "new end";
    description.innerHTML = "new description";
}