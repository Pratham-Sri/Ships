let myLeads = []
//Local storage only allows strings to be inserted, therfore for passing an array, we use json method stringify to convert array into a string and parse to convert string into an array.

const inputEl = document.getElementById("input-el")
const inputbtn = document.getElementById("input-btn")
const deletebtn = document.getElementById("delete-btn")
const ulEl = document.getElementById("ul-el")
const Tabbtn =document.getElementById("tab-btn")

//null -> used by developers to signify emptiness
// undefined -> used by javascript to signify emptiness

const myLeads_from_local_storage = JSON.parse(localStorage.getItem("myLeads"))

if(myLeads_from_local_storage){
    myLeads = myLeads_from_local_storage
    render(myLeads)
}

Tabbtn.addEventListener("click",function(){
    chrome.tabs.query({active : true , currentWindow : true}, function(tabs){
        myLeads.push(tabs[0].url)
        localStorage.setItem("myLeads",JSON.stringify(myLeads))
        render(myLeads)

    })
})
function render(leads){
    //using innerHTML
    let listItems = ""
    for( let i=0;i<leads.length;i++){
        listItems += `
        <li>
        <a target = '_blank' href = '${myLeads[i]}'>${myLeads[i]}</a>
        </li>`
    }
    ulEl.innerHTML = listItems

    //using createElement
    // for( let i = 0 ; i < myLeads.length ; i++){
    //      const li = document.createElement("li")
    //      li.textContent = myLeads[i]
    //      ulEl.append(li)
    // }
}

deletebtn.addEventListener("dblclick",function(){
    localStorage.clear()
    myLeads = []
    render(myLeads)
})
inputbtn.addEventListener("click" , function(){
    myLeads.push(inputEl.value)
    inputEl.value = "" 
    localStorage.setItem("myLeads",JSON.stringify(myLeads))  
    render(myLeads)
})
