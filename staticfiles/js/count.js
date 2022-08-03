function countTitle(){
    const input = document.getElementById('title').value;
    const output = document.getElementById('chars');
    let chars = input.length;
    if (!(chars > 150)){
        output.innerText = chars;
    } else {
        document.getElementById('title').disabled = true;
    }
}

function countDuration(){
    const input = document.getElementById('duration').value;
    const output = document.getElementById('time');
    let chars = input.length;
    if (!(chars > 50)){
        output.innerText = chars;
    } else {
        document.getElementById('duration').disabled = true;
    }
}

function Reset(){
    const title_field = document.getElementById('title');
    const duration_field = document.getElementById('duration');
    title_field.value = "";
    duration_field.value = "";
}