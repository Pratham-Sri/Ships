const apiKey ="402a8047a8a4aaa0c5a36d9e3352bfc8";
const apiUrl = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=Delhi";
async function checkweather(){
    const response = await fetch(apiUrl + `&appid=${apiKey}`);
    let data = await respose.json();
    document.querySelector(".city").innerHTML = data.name
    document.querySelector(".temp").innerHTML = data.main.temp;
    document.querySelector(".humidity").innerHTML = data.main.humidity;
    document.querySelector(".wind").innerHTML = data.wind.speed;
}