async function generate(){

const text=document.getElementById("text").value;
const voice=document.getElementById("voice").files[0];

const formData=new FormData();

formData.append("text",text);
formData.append("voice",voice);

const res=await fetch(
"https://YOUR_SERVER_URL/generate",
{
method:"POST",
body:formData
});

const blob=await res.blob();

document.getElementById("audio").src=
URL.createObjectURL(blob);
}
