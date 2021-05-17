var btn = document.getElementById("button");

btn.addEventListener("click", (event)=>{

    let newRecipeCard = document.getElementById("recipe_card");
    let titleValue = document.getElementById("title").value;
    let cuisineValue = document.getElementById("select_cuisine").value;
    let instructionsValue = document.getElementById("instructions").value;
    let servingsValue = document.getElementById("servings").value;
    let imageValue = document.getElementsByName("image").value;
    event.preventDefault();
    console.log("event Happening");

    let params = { "title" : titleValue, 
                    "cuisine" : cuisineValue,
                    "instructions" : instructionsValue,
                    "servings" : servingsValue,
                    "image" : imageValue,
                    "ingredients" : ingredientList };
    $.ajax({
        url: "/create_recipe/card",
        data: JSON.stringify(params),
        contentType: "application/json",
        method:"POST",
        success:(response)=>{
            newRecipeCard.innerHTML = response;
            console.log("success");
        }
    });
});