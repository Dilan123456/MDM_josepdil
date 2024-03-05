function inputChanged(event) {
    fetch('/square?n=' + event.target.value )
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById("result").value = data["square"];
        });
}