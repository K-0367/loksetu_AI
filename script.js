function showLoader(){
    document.getElementById("loader").classList.remove("hidden");
}

function hideLoader(){
    document.getElementById("loader").classList.add("hidden");
}

function typeText(text){
    let result = document.getElementById("result");
    result.innerHTML="";
    let i=0;

    function typing(){
        if(i<text.length){
            result.innerHTML+=text.charAt(i);
            i++;
            setTimeout(typing,20);
        }
    }
    typing();
}

function uploadFile(){
    let file=document.getElementById("fileInput").files[0];
    let formData=new FormData();
    formData.append("file",file);

    showLoader();

    fetch("http://127.0.0.1:5000/upload",{method:"POST",body:formData})
    .then(res=>res.json())
    .then(data=>{
        hideLoader();
        typeText(data.message);
    });
}

function sendText(){
    let text=document.getElementById("userText").value;

    showLoader();

    fetch("http://127.0.0.1:5000/text",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({text:text})
    })
    .then(res=>res.json())
    .then(data=>{
        hideLoader();
        typeText(data.message);
    });
}

function startVoice(){
    let recognition=new webkitSpeechRecognition();
    recognition.start();

    recognition.onresult=function(event){
        let speech=event.results[0][0].transcript;

        showLoader();

        fetch("http://127.0.0.1:5000/voice",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({text:speech})
        })
        .then(res=>res.json())
        .then(data=>{
            hideLoader();
            typeText(data.message);
        });
    }
}