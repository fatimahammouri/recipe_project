var ingredientList = [];

let addIngredientBtn = document.getElementById("add_ingredient"); // button element
let ingredientInputElement = document.getElementById("ingredients"); // input element
let ingredientValue = ingredientInputElement.value; // users input
let listElement = document.getElementById("input_ingredients"); // DOM ul element

addIngredientBtn.addEventListener("click", (event) => {
    ingredientValue = ingredientInputElement.value; 
    event.preventDefault(); 
    if (ingredientValue){
        console.log("ingredient added")
        ingredientList.push(ingredientValue);
    
        const element = document.createElement("li");
        element.textContent = ingredientValue;
        listElement.append(element);
        ingredientInputElement.value = "";
    }

});

////////////////////////////////////////////////////////////////////////////////////
var btn = document.getElementById("button");

btn.addEventListener("click", (event)=>{

    let newRecipeCard = document.getElementById("recipe_card");
    let titleValue = document.getElementById("title").value;
    let cuisineValue = document.getElementById("select_cuisine").value;
    let instructionsValue = document.getElementById("instructions").value;
    let servingsValue = document.getElementById("servings").value;
    let imageValue = $("#file").prop('files')[0];
    let readyTimeValue = document.getElementById("ready_in_minutes").value;
    event.preventDefault();
    console.log("event Happening");
    console.log(ingredientList)
    let form_data = new FormData();
    let ingList  = JSON.stringify(ingredientList);
    form_data.append("title" , titleValue) 
    form_data.append("cuisine" , cuisineValue)
    form_data.append("instructions" , instructionsValue)
    form_data.append("servings" , servingsValue)
    form_data.append("image" , imageValue)
    form_data.append("ingredients" , ingList) 
    form_data.append("ready_in_minutes" , readyTimeValue)
    console.log(form_data)           
    $.ajax({
        url: "/create_recipe/card",
        data: form_data,
        contentType: false,
        type:"POST",
        cache: false,
        processData: false,
        success:(response)=>{
            newRecipeCard.innerHTML = response;
            console.log("success");
        }
    });
});